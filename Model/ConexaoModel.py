import sqlite3


class ConexaoModel:
    def __init__(self):
        self.conexao = sqlite3.connect("Sistema de cadastro de cliente/Model/banco.db")
        self.cursor = self.conexao.cursor()

    
conexao = sqlite3.connect("Sistema de cadastro de cliente/Model/banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS login (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
            )""")

#cursor.execute("""INSERT INTO login 
#                (nome,senha) VALUES
#                ("Pedro","1234")""")

cursor.execute("""DELETE FROM login
                WHERE id = 2""")

conexao.commit()