from Model import ConexaoModel
from View import JanelaView

class Login:
    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha

    
    @staticmethod
    def verificarLogin(campo_usuario, campo_senha, resultado_login, janela_atual) -> None:
        usuario = campo_usuario.get()
        senha = campo_senha.get()
        
        Banco = ConexaoModel.ConexaoBanco()
        dados = Banco.TabelaUsuario()
        
        
        login_valido = any(linha[1] == usuario and linha[2] == senha for linha in dados)
        
        if login_valido:
            janela_atual.destroy()
            JanelaView.Janela("Clientes", 400, 400).exibir_clientes()
        else:
            resultado_login.configure(text="Login ou senha incorretos")

