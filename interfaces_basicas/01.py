import tkinter as tk
 
jan = tk.Tk()
jan.title('Testando')
jan.geometry('720x480')

texto = tk.Label(jan, text=f'Seja bem vindo(a)')
texto.pack()

def efeito():
    nome = entrada_txt.get()
    texto['text'] = f"E ai, {nome}!"
    
entrada_txt = tk.Entry(jan)
entrada_txt.pack()
tk.Button(jan, text='Aperta no butão', command=efeito).pack()

jan.mainloop()