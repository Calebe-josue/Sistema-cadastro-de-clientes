import customtkinter as ctk


class Janela:
    def __init__(self, titulo, largura, altura,cor="dark"):
        self.titulo = titulo
        self.largura = largura
        self.altura = altura
        self.cor = cor


    def exibir(self):
        ctk.set_appearance_mode(self.cor)
        app = ctk.CTk()
        app.title(self.titulo)
        app.geometry(f"{self.largura}x{self.altura}")
        #
        label_usuario = ctk.CTkLabel(app, text="Usuário:")
        label_usuario.pack(pady=10)
        #
        campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
        campo_usuario.pack(pady=10)
        #
        label_senha = ctk.CTkLabel(app, text="Senha:")
        label_senha.pack(pady=10) 
        #
        campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
        campo_senha.pack(pady=10)
        #
        botao_login = ctk.CTkButton(app, text="Login")
        botao_login.pack(pady=10)
        #
        resultado_login = ctk.CTkLabel(app, text="")
        resultado_login.pack(pady=10)

        app.mainloop()


