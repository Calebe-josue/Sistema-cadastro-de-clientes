import customtkinter as ctk
from Controller import LoginController

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
    def setLargura(self,largura) -> None:
        self.__largura=largura
    
    @property
    def getAltura(self) -> str:
        return self.__altura

    @getAltura.setter
    def setAltura(self,altura) -> None:
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
    


    def exibir_clientes(self):
        ctk.set_appearance_mode(self.cor)
        app = ctk.CTk()
        app.title(self.titulo)
        app.geometry(f"{self.getLargura}x{self.getAltura}")
        # label
        label_clientes = ctk.CTkLabel(app, text="Clientes:")
        label_clientes.pack(pady=10)
        # textbox para listar clientes
        textbox_clientes = ctk.CTkTextbox(app, width=300, height=200)
        textbox_clientes.pack(pady=10)
        textbox_clientes.insert("0.0", "Lista de clientes...")
        textbox_clientes.configure(state="disabled")
        # button
        botao_sair = ctk.CTkButton(app, text="Sair", command=app.destroy)
        botao_sair.pack(pady=10)
        app.mainloop()

