import customtkinter
from View import Janela
import sqlite3


conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS login (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
            )""")

# cursor.execute("""INSERT INTO login 
#                (nome,senha) VALUES
#                ("Pedro","1234")""")

cursor.execute("""SELECT * FROM login""")
contas = cursor.fetchall()
print(contas)

conexao.commit()

login = Janela.Janela("Minha Janela", 300, 300)

login.exibir()

