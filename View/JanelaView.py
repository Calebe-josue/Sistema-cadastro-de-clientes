import customtkinter as ctk
from Controller import LoginController
from Model import ConexaoModel

class Janela:
    def __init__(self, titulo, largura, altura, cor="dark"):
        self.titulo = titulo
        self.__largura = largura
        self.__altura = altura
        self.cor = cor

    @property
    def getLargura(self) -> str:
        return self.__largura

    @getLargura.setter
    def setLargura(self, largura) -> None:
        self.__largura = largura
    
    @property
    def getAltura(self) -> str:
        return self.__altura

    @getAltura.setter
    def setAltura(self, altura) -> None:
        self.__altura = altura


    def exibir_login(self) -> None:
        ctk.set_appearance_mode(self.cor)
        app = ctk.CTk()
        app.title(self.titulo)
        app.geometry(f"{self.getLargura}x{self.getAltura}")
        # label
        label_usuario = ctk.CTkLabel(app, text="Usuário:")
        label_usuario.pack(pady=10)
        # entry
        campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
        campo_usuario.pack(pady=10)
        # label
        label_senha = ctk.CTkLabel(app, text="Senha:")
        label_senha.pack(pady=10) 
        # entry
        campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
        campo_senha.pack(pady=10)
        #label
        resultado_login = ctk.CTkLabel(app, text="")
        resultado_login.pack(pady=10)
        
        # button
        botao_login = ctk.CTkButton(app, text="Login", command=lambda: LoginController.Login.verificarLogin(campo_usuario, campo_senha, resultado_login, app))
        botao_login.pack(pady=10)

        app.mainloop()
    

    @staticmethod
    def atualizar_lista(textbox) -> None:
        banco = ConexaoModel.ConexaoBanco()
        clientes = banco.TabelaClientes()
        
        textbox.delete("1.0", "end")
        
        if not clientes:
            textbox.insert("end", "Nenhum cliente cadastrado.")
            return
        
        # Cabeçalho
        textbox.insert("end", f"{'ID':<5} {'Nome':<20} {'Email':<25} {'Telefone':<15}\n")
        textbox.insert("end", "-" * 70 + "\n")
        
        for cliente in clientes:
            id_, nome, email, telefone = cliente
            linha = f"{id_:<5} {nome:<20} {email:<25} {telefone:<15}\n"
            textbox.insert("end", linha)


    def exibir_clientes(self):
        ctk.set_appearance_mode(self.cor)
        app = ctk.CTk()
        app.geometry(f"{540}x{420}")
        # Título
        titulo = ctk.CTkLabel(app, text="Sistema de Clientes", font=("Arial", 18))
        titulo.pack(pady=10)

        # ===== FORMULÁRIO =====
        entry_nome = ctk.CTkEntry(app, placeholder_text="Nome")
        entry_nome.pack(pady=5)

        entry_email = ctk.CTkEntry(app, placeholder_text="Email")
        entry_email.pack(pady=5)

        entry_telefone = ctk.CTkEntry(app, placeholder_text="Telefone")
        entry_telefone.pack(pady=5)

        # Label de status/feedback
        label_status = ctk.CTkLabel(app, text="", font=("Arial", 12))
        label_status.pack(pady=5)

        # ===== BOTÕES =====
        frame_botoes = ctk.CTkFrame(app)
        frame_botoes.pack(pady=10)

        btn_cadastrar = ctk.CTkButton(
            frame_botoes, 
            text="Cadastrar", 
            command=lambda: LoginController.Login.Criarcliente(
                entry_nome, entry_email, entry_telefone, label_status, l_lista
            )
        )
        btn_cadastrar.pack(side="left", padx=5)

        btn_buscar = ctk.CTkButton(
            frame_botoes, 
            text="Atualizar", 
            command=lambda: Janela.atualizar_lista(l_lista)
        )
        btn_buscar.pack(side="left", padx=5)

        # ===== LISTA =====
        l_lista = ctk.CTkTextbox(app, width=500, height=200)
        l_lista.pack(pady=10)

        # Preenche a lista automaticamente ao abrir
        Janela.atualizar_lista(l_lista)

        app.mainloop()

