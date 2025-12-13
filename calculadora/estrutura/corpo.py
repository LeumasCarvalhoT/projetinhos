
valores = ''
def esqueleto():
    from tkinter import Frame, Tk, StringVar, Label, Button, RAISED, RIGHT, FLAT, RIDGE 
    from tkinter import ttk
    cor1 = '#23241f'
    cor2 = '#f5f3c9'
    cor3 = '#fffffc'
    cor4 = '#010329'
    cor5 = '#e3aa39'

    window = Tk()
    window.title('Calculadora Básica')
    window.geometry('247x355')

    frame_tela = Frame(window, width='247', height='60')
    frame_tela.grid(row=0, column=0)

    frame_corpo = Frame(window, width='247', height= '300', bg=cor2)
    frame_corpo.grid(row=1, column=0)
    
    def entrada(v):
        global valores
        valores = valores + str(v)
        entrada_str.set(valores)

    def calculos():
        global valores
        resultado = eval(valores)
        print(resultado)
        entrada_str.set(str(resultado))

    def limpador():
        global valores
        valores = ''
        entrada_str.set('')

    entrada_str = StringVar()

    barra_label = Label(frame_tela, textvariable=entrada_str, width='33', height='3', padx='7', anchor="e", relief=FLAT, justify=RIGHT, bg=cor4, fg=cor3, font=('ivy 16'))
    barra_label.place(x=-166, y=0)

    b_1 = Button(frame_corpo, command= limpador,text='C', width=11, height=2,bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_1.place(x=0,y=0)
    b_2 = Button(frame_corpo, command=lambda: entrada('%'), text='%', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_2.place(x=122,y=0)
    b_3 = Button(frame_corpo, command=lambda: entrada('/'),text='/', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_3.place(x=185,y=0)

    b_4 = Button(frame_corpo, command=lambda: entrada('7'),text='7', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_4.place(x=0,y=60)
    b_5 = Button(frame_corpo, command=lambda: entrada('8'),text='8', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_5.place(x=61,y=60)
    b_6 = Button(frame_corpo, command=lambda: entrada('9'),text='9', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_6.place(x=122,y=60)
    b_7 = Button(frame_corpo, command=lambda: entrada('*'),text='*', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_7.place(x=185,y=60)

    b_8 = Button(frame_corpo, command=lambda: entrada('4'),text='4', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_8.place(x=0,y=120)
    b_9 = Button(frame_corpo, command=lambda: entrada('5'),text='5', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_9.place(x=61,y=120)
    b_10 = Button(frame_corpo, command=lambda: entrada('6'),text='6', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_10.place(x=122,y=120)
    b_11= Button(frame_corpo, command=lambda: entrada('-'),text='-', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_11.place(x=185,y=120)

    b_12 = Button(frame_corpo, command=lambda: entrada('1'),text='1', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_12.place(x=0,y=180)
    b_13 = Button(frame_corpo, command=lambda: entrada('2'),text='2', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_13.place(x=61,y=180)
    b_14 = Button(frame_corpo, command=lambda: entrada('3'),text='3', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_14.place(x=122,y=180)
    b_15= Button(frame_corpo, command=lambda: entrada('+'),text='+', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_15.place(x=185,y=180)

    b_16 = Button(frame_corpo, command=lambda: entrada('0'),text='0', width=11, height=2,bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_16.place(x=0,y=240)
    b_17= Button(frame_corpo, command=lambda: entrada('.'),text='.', width=5, height=2, bg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_17.place(x=122,y=240)
    b_18 = Button(frame_corpo, command= calculos,text='=', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b_18.place(x=185,y=240)

    window.mainloop()

esqueleto()
