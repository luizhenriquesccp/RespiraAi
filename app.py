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

# ROTA CORRIGIDA E FUNCIONAL
@app.route("/salvar_pratica", methods=['POST'])
def salvar_pratica():
    # 1. Verificar se o usuário está logado na sessão
    usuario_atual = session.get('usuario')
    if not usuario_atual:
        return jsonify({'success': False, 'message': 'Usuário não autenticado. Faça login novamente.'}), 401

    # 2. Obter os dados enviados pelo JavaScript
    data = request.get_json()
    if not data or 'tempo_segundos' not in data or 'id_exercicio' not in data:
        return jsonify({'success': False, 'message': 'Dados da prática estão incompletos.'}), 400

    conn = None
    try:
        # 3. Conectar ao banco de dados
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        # 4. Obter o ID do usuário a partir do email na sessão
        cursor.execute("SELECT id FROM usuario WHERE email = %s", (usuario_atual,))
        user = cursor.fetchone()
        if not user:
            return jsonify({'success': False, 'message': 'Usuário não encontrado no banco de dados.'}), 404
        
        id_usuario = user['id']
        id_exercicio = data.get('id_exercicio')
        tempo_segundos = data.get('tempo_segundos')

        # 5. Converter o tempo de segundos para minutos (arredondando)
        # Se o tempo for menor que 30s, salva como 0 min. Se for 30s ou mais, salva como 1 min.
        tempo_minutos = round(tempo_segundos / 60)
        
        # Se quiser salvar pelo menos 1 minuto para qualquer prática, use math.ceil
        # from math import ceil
        # tempo_minutos = ceil(tempo_segundos / 60) if tempo_segundos > 0 else 0

        cursor.execute(
            "INSERT INTO pratica (data, tempo_dedicado, id_usuario, id_exercicio) VALUES (%s, %s, %s, %s)",
            (datetime.now(), tempo_minutos, id_usuario, id_exercicio)
        )
        conn.commit() 
        
        return jsonify({'success': True, 'message': 'Prática salva com sucesso!'})

    except mysql.connector.Error as err:
        return jsonify({'success': False, 'message': f'Erro no banco de dados: {err}'}), 500
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
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
    cursor.execute("SELECT * FROM exercicio ORDER BY id_exercicio ASC")
    exercicios = cursor.fetchall()
    cursor.close()
    conn.close()
    if exercicios:
        primeiro_id = exercicios[0]['id_exercicio']
        return redirect(url_for('exibir_exercicio', id=primeiro_id))
    else:
        flash("Nenhum exercício cadastrado.")
        return render_template("ex.html", exercicios=[], exercicio={})

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
