import tkinter as tk

contas = [('Samuca', '696969'),
          ('Gabriel','C0CK')
            ]

def login():
    usu = usu_entrada.get()
    Senha = Senha_entrada.get()
    if (usu, Senha) in contas:
        pag_login.pack_forget()
        pag_sistem.pack()
    else:
        mensagem['text'] = 'Usuário ou senha incorreta!'


jan = tk.Tk()
jan.title('Login')
jan.geometry("720x480")

pag_login = tk.Frame(jan)
pag_login.pack()

pag_sistem = tk.Frame()
tk.Label(pag_sistem, text='Seja bem vindo ao sistema').pack()

tk.Label(pag_login, text='Usuário').pack()
usu_entrada = tk.Entry(pag_login)
usu_entrada.pack()

tk.Label(pag_login, text='Senha').pack()
Senha_entrada = tk.Entry(pag_login)
Senha_entrada.pack()

tk.Button(pag_login, text='Login', command=login).pack()
mensagem = tk.Label(pag_login, text='')
mensagem.pack()

jan.mainloop()