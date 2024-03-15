import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def login():
    print("Login clicado")
    

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Login criado por Gabriel")  

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
email = customtkinter.CTkEntry(janela, placeholder_text="Email-")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(janela, text="Login", command=login)

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

janela.mainloop()



janela.mainloop()
