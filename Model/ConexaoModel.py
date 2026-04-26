import sqlite3
import os


class ConexaoBanco:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), "banco.db")

    def _conectar(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        return conexao, cursor

    def CriarTabelaUsuario(self) -> None:
        conexao, cursor = self._conectar()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
            )""")
        
        # verifica se já existe
        cursor.execute("SELECT * FROM login WHERE nome = ? AND senha = ?", ("Calebe", "1234"))
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO login (nome, senha) VALUES (?, ?)",
                ("Calebe", "1234")
            )

        conexao.commit()
        conexao.close()

    
    def TabelaUsuario(self) -> list:
        self.CriarTabelaUsuario()
        conexao, cursor = self._conectar()
        cursor.execute("SELECT * FROM login")
        dados = cursor.fetchall()
        conexao.close()
        return dados

    
    def CriarTabelaClientes(self) -> None:
        conexao, cursor = self._conectar()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL 
            )""")       
        conexao.commit()
        conexao.close()
      

    def cadastrar_cliente(self, nome, email, telefone) -> str:
        self.CriarTabelaClientes()
        conexao, cursor = self._conectar()
        cursor.execute("""
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()
        conexao.close()
        return "Cliente cadastrado com sucesso!"


    def TabelaClientes(self) -> list:
        self.CriarTabelaClientes()
        conexao, cursor = self._conectar()
        cursor.execute("SELECT * FROM clientes")
        dados = cursor.fetchall()
        conexao.close()
        return dados

