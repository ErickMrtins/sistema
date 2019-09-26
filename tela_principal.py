from tkinter import *


class TelaPrincipal:

    def __init__(self, master):

        self.master = master
        self.lb_titulo = Label(master, text='Tela Principal', bg='blue')
        self.lb_titulo.pack(side=TOP, fill=BOTH)

        self.menu_lateral = Frame(master, bg='white', width=150, height=460)
        self.menu_lateral.place(x=5, y=30)

        self.button_cadastrar = Button(self.menu_lateral, text='Cadastro', width=18, height=2, bd=5, command=self.btn_cadastro_click)
        self.button_cadastrar.place(x=5, y=10)

        self.button_consultar = Button(self.menu_lateral, text='Consultar', width=18, height=2, bd=5, command=self.btn_consulta_click)
        self.button_consultar.place(x=5, y=60)

        self.frame_principal = Frame(master, bg='#CDC9C9', width=335, height=460)
        self.frame_principal.place(x=160, y=30)

        self.label_titulo_frame = Label(self.frame_principal, text='', bg='#CDC9C9', width=20, font=("Broadway", 11))
        self.label_titulo_frame.place(x=80, y=5)



    def mostra_tela_principal():
        root = Tk()
        TelaPrincipal(root)
        root.geometry('500x500')
        root.resizable(0, 0)
        root.title('Sistema')
        root.mainloop()


    def btn_cadastro_click(self):
        self.label_titulo_frame['text'] = 'Cadastro'
        self.imagem = PhotoImage(file='C:/Users/martinser/Pictures/cadastro.png')
        self.imagem_label = Label(self.frame_principal, image=self.imagem, bg='#CDC9C9')
        self.imagem_label.place(x=5, y=2)

    def btn_consulta_click(self):
        self.label_titulo_frame['text'] = 'Consulta'
        self.imagem = PhotoImage(file='C:/Users/martinser/Pictures/cadastro.png')
        self.imagem_label = Label(self.frame_principal, image=self.imagem, bg='#CDC9C9')
        self.imagem_label.place(x=5, y=2)


