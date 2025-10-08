from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from datetime import datetime
import mysql.connector

app = Flask(__name__)
app.secret_key = 'respira_ai_secret_key_2024'

def get_db():
    return mysql.connector.connect(
        user="root",
        password="labinfo",
        database="setembroamarelo",
        host="127.0.0.1"
    )

@app.route("/")
def index():
    usuario_atual = session.get('usuario')
    if not usuario_atual:
        return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome FROM usuario WHERE email = %s", (usuario_atual,))
    user = cursor.fetchone()
    if not user:
        cursor.close()
        conn.close()
        flash("Usuário não encontrado. Faça login novamente.")
        return redirect(url_for('login'))
    cursor.execute("""
        SELECT p.tempo_dedicado, p.data
        FROM pratica p
        WHERE p.id_usuario = %s
    """, (user['id'],))
    praticas_usuario = cursor.fetchall()
    total_minutos = sum([p['tempo_dedicado'] or 0 for p in praticas_usuario])
    qtd_praticas = len(praticas_usuario)
    media = total_minutos / qtd_praticas if qtd_praticas > 0 else 0

    estatisticas = {
        'totalMinutos': round(total_minutos, 1),
        'qtdPraticas': qtd_praticas,
        'media': round(media, 1)
    }
    cursor.close()
    conn.close()
    return render_template("index.html", estatisticas=estatisticas, usuario=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    usuario = request.form.get('user')
    senha = request.form.get('pass')
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email = %s AND senha = %s", (usuario, senha))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        session['usuario'] = usuario
        return redirect(url_for('index'))
    else:
        flash('Usuário ou senha incorretos')
        return render_template("login.html", erro="Usuário ou senha incorretos")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template("cadastro.html")
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return render_template("cadastro.html", erro="E-mail já cadastrado")
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('login'))

@app.route("/historico")
def historico():
    usuario_atual = session.get('usuario')
    if not usuario_atual:
        return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.data, p.tempo_dedicado, e.nome AS exercicio
        FROM pratica p
        JOIN usuario u ON p.id_usuario = u.id
        JOIN exercicio e ON p.id_exercicio = e.id_exercicio
        WHERE u.email = %s
        ORDER BY p.data DESC
    """, (usuario_atual,))
    praticas_usuario = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("h.html", praticas=praticas_usuario)

@app.route("/salvar_pratica", methods=['POST'])
def salvar_pratica():
    data = request.get_json()
    usuario_atual = session.get('usuario')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuario WHERE email = %s", (usuario_atual,))
    user = cursor.fetchone()
    if not user:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': 'Usuário não encontrado'})
    id_usuario = user[0]
    cursor.execute("SELECT id_exercicio FROM exercicio WHERE nome = %s", (data.get('exercicio'),))
    ex = cursor.fetchone()
    if not ex:
        cursor.close()
        conn.close()
        return jsonify({'success': False, 'message': 'Exercício não encontrado'})
    id_exercicio = ex[0]
    tempo = int(data.get('tempo', '0').split(':')[0])  # minutos
    cursor.execute(
        "INSERT INTO pratica (data, tempo_dedicado, id_usuario, id_exercicio) VALUES (%s, %s, %s, %s)",
        (datetime.now(), tempo, id_usuario, id_exercicio)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'success': True, 'message': 'Prática salva com sucesso'})

@app.route("/logout")
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route("/exercicios")
def lista_exercicios():
    usuario_atual = session.get('usuario')
    if not usuario_atual:
        return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM exercicio")
    exercicios = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("ex.html", exercicios=exercicios, exercicio={})

@app.route("/exercicio/<int:id>")
def exibir_exercicio(id):
    usuario_atual = session.get('usuario')
    if not usuario_atual:
        return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM exercicio WHERE id_exercicio = %s", (id,))
    exercicio = cursor.fetchone()
    cursor.execute("SELECT * FROM exercicio")
    exercicios = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("ex.html", exercicio=exercicio, exercicios=exercicios)
