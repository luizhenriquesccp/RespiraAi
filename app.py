from flask import Flask, render_template
from mysql.connector import connection

app = Flask(__name__)

@app.route("/")
def lista_exercicios():
    
    cnx = connection.MySQLConnection(
        user="root",
        password="labinfo",
        database="respiraai", 
        host="127.0.0.1"
    )

    cursor = cnx.cursor(dictionary=True)

    
    sql = "SELECT nome, descriçao, duraçao FROM exercicio"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    cnx.close()

    return render_template("exercicio.html", banco=resultado)

@app.route("/exercicio/<int:id>")
def exibir_exercicio(id):
    cnx = connection.MySQLConnection(
        user="root",
        password="labinfo",
        database="respiraai", 
        host="127.0.0.1"
    )
    cursor = cnx.cursor(dictionary=True)
    sql = "SELECT nome, descriçao as descricao, duraçao as duracao FROM exercicio WHERE id = %s"
    cursor.execute(sql, (id,))
    resultado = cursor.fetchone()
    cursor.close()
    cnx.close()
    return render_template("ex.html", exercicio=resultado)
