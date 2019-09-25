from tkinter import *


class TelaPrincipal:

    def __init__(self, master):

        self.master = master
        self.lb_titulo = Label(master, text='Tela Principal', bg='blue')
        self.lb_titulo.pack(side=TOP, fill=BOTH)

        self.menu_lateral = Frame(master, bg='white', width=150, height=460)
        self.menu_lateral.place(x=5, y=30)

    def mostra_tela_principal():
        root = Tk()
        TelaPrincipal(root)
        root.geometry('500x500')
        root.resizable(0, 0)
        root.title('Sistema')
        root.mainloop()




