import sqlite3
import os


class ConexaoBanco:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), "banco.db")
        self.conexao = sqlite3.connect(db_path)
        self.cursor = self.conexao.cursor()


    def CriarTabelaUsuario(self) -> None:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
            )""")
        
        # verifica se já existe
        self.cursor.execute("SELECT * FROM login WHERE nome = ? AND senha = ?", ("Calebe", "1234"))
        if not self.cursor.fetchone():
            self.cursor.execute(
            """INSERT INTO login (nome, senha) VALUES
            ("Calebe", "1234")"""
        )

        self.conexao.commit()

    
    def TabelaUsuario(self) -> tuple:
        self.CriarTabelaUsuario()
        self.cursor.execute("SELECT * FROM login")
        dados = self.cursor.fetchall()
        return dados



    def CriarTabelaClientes(self) -> None:
        
    
      



# cursor.execute("""DELETE FROM login
#                 WHERE id = 2""")

# conexao.commit()
