import os
from tkinter.filedialog import askdirectory

guia = askdirectory(title='')
lista_arq = os.listdir(guia)
tipos_arq = {'imagens': ['.png', '.jpg', '.jpeg'],
             'planilhas': ['.xlsx'],
             'pdfs': ['.pdf'],
             'compactados': ['.rar','.zip']}
for arq in lista_arq:
    nome, tip = os.path.splitext(f'{guia}/{arq}')
    for pasta in tipos_arq:
        if tip in tipos_arq[pasta]:
            if not os.path.exists(f'{guia}/{pasta}'):
                os.mkdir(f'{guia}/{pasta}')
            os.rename(f'{guia}/{arq}', f'{guia}/{pasta}/{arq}')



