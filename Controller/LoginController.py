from Model import ConexaoModel
from View import JanelaView


class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    
    @staticmethod
    def verificarLogin(campo_usuario, campo_senha, resultado_login, janela_atual) -> None:
        usuario = campo_usuario.get().strip()
        senha = campo_senha.get().strip()
        
        if not usuario or not senha:
            resultado_login.configure(text="Preencha todos os campos")
            return
        
        Banco = ConexaoModel.ConexaoBanco()
        dados = Banco.TabelaUsuario()
        
        login_valido = any(linha[1] == usuario and linha[2] == senha for linha in dados)
        
        if login_valido:
            janela_atual.destroy()
            JanelaView.Janela("Clientes", 400, 400).exibir_clientes()
        else:
            resultado_login.configure(text="Login ou senha incorretos")

    @staticmethod
    def Criarcliente(campo_nome, campo_email, campo_telefone, label_status, lista_textbox) -> None:
        nome = campo_nome.get().strip()
        email = campo_email.get().strip()
        telefone = campo_telefone.get().strip()

        if not nome or not email or not telefone:
            label_status.configure(text="Preencha todos os campos", text_color="red")
            return

        banco = ConexaoModel.ConexaoBanco()
        mensagem = banco.cadastrar_cliente(nome, email, telefone)
        
        # Limpa os campos
        campo_nome.delete(0, "end")
        campo_email.delete(0, "end")
        campo_telefone.delete(0, "end")
        
        label_status.configure(text=mensagem, text_color="green")
        
        # Atualiza a lista automaticamente
        JanelaView.Janela.atualizar_lista(lista_textbox)

