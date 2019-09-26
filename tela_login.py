from tkinter import *
from tela_principal import TelaPrincipal


class App:

    def limpar_entrada_login(self, event):
        self.ed_login.delete(0, END)

    def limpar_entrada_senha(self, event):
        self.ed_senha.delete(0, END)
        self.ed_senha.config(show='*')

    def btn_logar_click(self):

        if self.ed_login.get() == 'admin' and self.ed_senha.get() == 'admin':
            root.destroy()
            TelaPrincipal.mostra_tela_principal()
        else:
            print('Login falhou!')

    def __init__(self, master):

        self.Frame = Frame(master, bg='white', width=200, height=200)
        self.Frame.place(x=50, y=50)

        self.label_titulo = Label(master, text='Bem Vindo ao Sistema', bg='blue', fg='white', height=1)
        self.label_titulo.pack(side=TOP, fill=BOTH)

        self.label_login = Label(self.Frame, text='Login', font=("Mistral", 20), bg='white')
        self.label_login.place(x=75, y=0)

        self.ed_login = Entry(self.Frame)
        self.ed_login.insert(0, 'Usuário')
        self.ed_login.bind("<Button-1>", self.limpar_entrada_login)
        self.ed_login.place(x=40, y=70)

        self.ed_senha = Entry(self.Frame)
        self.ed_senha.insert(0, 'Senha')
        self.ed_senha.bind("<Button-1>", self.limpar_entrada_senha)
        self.ed_senha.place(x=40, y=100)

        self.btn_logar = Button(self.Frame, text='Entrar', bg='gray', command=self.btn_logar_click)
        self.btn_logar.place(x=75, y=150)


        master.title('Login')


root = Tk()
App(root)
root.resizable(0, 0)
root.geometry('300x300+200+200')
root.iconbitmap('C:/Users/martinser/Pictures/cadastro.ico')
root.mainloop()


