from datetime import datetime

from app import app, db
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.models import Exercicio, Pratica, Usuario
from app.services.AuthenticationService import AuthenticationService

@app.route("/")
def index():
    usuario_atual = session.get("usuario")
    if not usuario_atual:
        return redirect(url_for("login"))

    with db.session() as db_session:
        user = db_session.scalar(
            select(Usuario).where(Usuario.email == usuario_atual)
        )
        if not user:
            flash("Usuário não encontrado. Faça login novamente.")
            return redirect(url_for("login"))

        praticas_usuario = db_session.scalars(
            select(Pratica).where(Pratica.id_usuario == user.id)
        ).all()

    total_minutos = sum(pratica.tempo_dedicado or 0 for pratica in praticas_usuario)
    qtd_praticas = len(praticas_usuario)
    media = total_minutos / qtd_praticas if qtd_praticas > 0 else 0
    estatisticas = {
        "totalMinutos": round(total_minutos, 1),
        "qtdPraticas": qtd_praticas,
        "media": round(media, 1),
    }
    return render_template("index.html", estatisticas=estatisticas, usuario=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    senha = request.form.get("pass")
    with db.session() as db_session:
        user = AuthenticationService.login(db_session, email, senha)

    if user:
        session["usuario"] = user.email
        return redirect(url_for("index"))

    flash("Usuário ou senha incorretos")
    return render_template("login.html", erro="Usuário ou senha incorretos")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")

    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario_existente = db.session.scalar(
        select(Usuario).where(Usuario.email == email)
    )
    if usuario_existente:
        return render_template("cadastro.html", erro="E-mail já cadastrado")

    try:
        db.session.add(Usuario(nome=nome, email=email, senha=senha))
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        app.logger.exception("Erro ao cadastrar usuário")
        return render_template(
            "cadastro.html",
            erro="Não foi possível cadastrar o usuário.",
        )

    return redirect(url_for("login"))


@app.route("/historico")
def historico():
    usuario_atual = session.get("usuario")
    if not usuario_atual:
        return redirect(url_for("login"))

    with db.session() as db_session:
        praticas = db_session.scalars(
            select(Pratica)
            .join(Pratica.usuario)
            .join(Pratica.exercicio)
            .where(Usuario.email == usuario_atual)
            .order_by(Pratica.data.desc())
        ).all()

        praticas_usuario = [
            {
                "data": pratica.data,
                "tempo_dedicado": pratica.tempo_dedicado,
                "exercicio": pratica.exercicio.nome if pratica.exercicio else None,
            }
            for pratica in praticas
        ]

    return render_template("h.html", praticas=praticas_usuario)


@app.route("/salvar_pratica", methods=["POST"])
def salvar_pratica():
    usuario_atual = session.get("usuario")
    if not usuario_atual:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Usuário não autenticado. Faça login novamente.",
                }
            ),
            401,
        )

    data = request.get_json(silent=True)
    if not data or "tempo_segundos" not in data or "id_exercicio" not in data:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Dados da prática estão incompletos.",
                }
            ),
            400,
        )

    try:
        id_exercicio = int(data["id_exercicio"])
        tempo_segundos = float(data["tempo_segundos"])
    except (TypeError, ValueError):
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Dados da prática são inválidos.",
                }
            ),
            400,
        )

    with db.session() as db_session:
        user = db_session.scalar(
            select(Usuario).where(Usuario.email == usuario_atual)
        )
        if not user:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Usuário não encontrado no banco de dados.",
                    }
                ),
                404,
            )

        exercicio = db_session.get(Exercicio, id_exercicio)
        if not exercicio:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Exercício não encontrado no banco de dados.",
                    }
                ),
                404,
            )

        pratica = Pratica(
            data=datetime.now(),
            tempo_dedicado=round(tempo_segundos / 60),
            usuario=user,
            exercicio=exercicio,
        )
        db_session.add(pratica)
        try:
            db_session.commit()
        except SQLAlchemyError:
            db_session.rollback()
            app.logger.exception("Erro ao salvar prática")
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Não foi possível salvar a prática.",
                    }
                ),
                500,
            )

    return jsonify({"success": True, "message": "Prática salva com sucesso!"})


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))


@app.route("/exercicios")
def lista_exercicios():
    usuario_atual = session.get("usuario")
    if not usuario_atual:
        return redirect(url_for("login"))

    with db.session() as db_session:
        exercicios = db_session.scalars(
            select(Exercicio).order_by(Exercicio.id_exercicio.asc())
        ).all()

    if exercicios:
        return redirect(
            url_for("exibir_exercicio", id=exercicios[0].id_exercicio)
        )

    flash("Nenhum exercício cadastrado.")
    return render_template("ex.html", exercicios=[], exercicio={})


@app.route("/exercicio/<int:id>")
def exibir_exercicio(id):
    usuario_atual = session.get("usuario")
    if not usuario_atual:
        return redirect(url_for("login"))

    with db.session() as db_session:
        exercicio = db_session.get(Exercicio, id)
        exercicios = db_session.scalars(
            select(Exercicio).order_by(Exercicio.id_exercicio.asc())
        ).all()

    if not exercicio:
        flash("Exercício não encontrado.")
        return redirect(url_for("lista_exercicios"))

    return render_template(
        "ex.html",
        exercicio=exercicio,
        exercicios=exercicios,
    )
