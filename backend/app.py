from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Conexão com o banco de dados PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='seu_banco_de_dados',
        user='seu_usuario',
        password='sua_senha'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Adicione rotas para lidar com compras e fornecedores aqui

if __name__ == '__main__':
    app.run(debug=True)
