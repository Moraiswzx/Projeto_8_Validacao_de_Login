import sqlite3

nome_banco = 'cadastro.db'


script_tabela = """CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
                password TEXT NOT NULL
            );"""
            

try:
    with sqlite3.connect(nome_banco) as conn:
        # Cria um cursor
        cur = conn.cursor()

        # Executa o script
        cur.execute(script_tabela)

        # Salva as alterações no banco de dados
        conn.commit()

        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)
