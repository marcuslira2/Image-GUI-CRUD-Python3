import ntpath
import os
import sqlite3
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog as fd
from PIL import Image, ImageTk

import bd


class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("App")
        bd.bd.abrirConexao(self)
        self._frame = None
        self.trocar_tela(Login)

    def trocar_tela(self, frame_class):
        ## Troca de frame
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Login(tk.Frame):
    tentativas = 0

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Criando os componentes da tela login
        tk.Label(self, text="Login")
        self.login = tk.Label(self, text="Login")
        self.txt_login = tk.Entry(self)
        self.pwd = tk.Label(self, text="Senha")
        self.txt_pwd = tk.Entry(self, show="*")
        self.cadastro = tk.Button(self, text="Cadastro",
                                  command=lambda: master.trocar_tela(Cadastro))
        self.entrar = tk.Button(self, text="Entrar",
                                command=lambda: self.verificar(master))

        self.login.pack()
        self.txt_login.pack()
        self.pwd.pack()
        self.txt_pwd.pack()
        self.entrar.pack()
        self.cadastro.pack()

    def verificar(self, master):

        try:
            user = self.txt_login.get().strip()
            pwd = self.txt_pwd.get().strip()
            acesso = bd.bd.select_user(self, user)
            if user in acesso[2] and pwd in acesso[3] and pwd != '':
                global usuario_sessao
                usuario_sessao = user
                print(usuario_sessao)
                master.trocar_tela(Principal)
                self.tentativas = 0
            elif user in acesso[2] and pwd not in acesso[3]:
                self.tentativas += 1
                if self.tentativas < 5:
                    tk.messagebox.showinfo("Alert",
                                           f"Senha errada, tente novametne, numero de tentativas restantes {5 - self.tentativas}")
                if self.tentativas >= 5:
                    self.txt_login.get()
                    tk.messagebox.showinfo("Alert", "Usuario bloqueado por 1 minuto")
                    self.tentativas = 0
                else:
                    print('erro')
            else:
                print("Usuario não encontrado")

        except Exception as erro:
            print('erro:', erro)


class Cadastro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Criando os componetes da tela cadastro
        self.titulo = tk.Label(self, text="Cadastro")
        self.lb_name = tk.Label(self, text="Nome")
        self.txt_name = tk.Entry(self)
        self.lb_cpf = tk.Label(self, text="Cpf")
        self.txt_cpf = tk.Entry(self)
        self.lb_user = tk.Label(self, text="Usuario")
        self.txt_user = tk.Entry(self)
        self.lb_pwd = tk.Label(self, text="Senha")
        self.txt_pwd = tk.Entry(self)
        self.cadastro = tk.Button(self, text="Cadastrar",
                                  command=lambda: [self.cadastrar_pessoa(), self.msgbox(),
                                                   master.trocar_tela(Login)])
        self.voltar = tk.Button(self, text="Voltar",
                                command=lambda: master.trocar_tela(Login))

        self.titulo.pack()
        self.lb_name.pack()
        self.txt_name.pack()
        self.lb_cpf.pack()
        self.txt_cpf.pack()
        self.lb_user.pack()
        self.txt_user.pack()
        self.lb_pwd.pack()
        self.txt_pwd.pack()
        self.cadastro.pack()
        self.voltar.pack()

    def msgbox(self):
        tk.messagebox.showinfo("Sucess", "Usuario cadastrado com sucesso")

    def lercampos(self):
        try:
            name = self.txt_name.get()
            cpf = self.txt_cpf.get()
            user = self.txt_user.get()
            pwd = self.txt_pwd.get()
        except:
            print("não foi possivel ler os dados")
        return name, cpf, user, pwd

    def cadastrar_pessoa(self):
        try:
            name, cpf, user, pwd = self.lercampos()
            bd.bd.insert_user(self, name, cpf, user, pwd)
        except Exception as erro:
            print("não foi possivel fazer o cadastro: ", erro)


class Principal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        print(usuario_sessao)

        self.tela = tk.Label(self, text="Tela principal")
        self.img01 = tk.Canvas(self, width=150, height=150, bg='red')
        self.img02 = tk.Canvas(self, width=150, height=150, bg='green')
        self.img03 = tk.Canvas(self, width=150, height=150, bg='blue')
        self.img04 = tk.Canvas(self, width=150, height=150, bg='blue')
        self.img05 = tk.Canvas(self, width=150, height=150, bg='red')
        self.img06 = tk.Canvas(self, width=150, height=150, bg='green')
        self.img07 = tk.Canvas(self, width=150, height=150, bg='green')
        self.img08 = tk.Canvas(self, width=150, height=150, bg='blue')
        self.img09 = tk.Canvas(self, width=150, height=150, bg='red')

        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            select = """SELECT * FROM imagem WHERE user =?"""
            cursor.execute(select, [usuario_sessao])
            result = cursor.fetchall()
            print(result)

        except Exception as erro:
            print(erro)
        finally:
            if connection:
                cursor.close()
                connection.close()
        self.caminho = result
        print(len(self.caminho))
        self.lista = {}
        try:
            for i in range(len(result)):
                checagem = os.path.isfile(result[i][2])
                while True:
                    if checagem:
                        self.lista[i] = tk.PhotoImage(file=result[i][2])
                        break
                    else:
                        mensagem = tkinter.messagebox.askquestion('Aviso',
                                                                  f'Imagem não encontrada no grid{i + 1}\ndeseja deletar?',
                                                                  icon='warning')
                        if mensagem == 'yes':
                            self.deletar_imagem(master, result[i][2], result[i][0], result[i][1])

                            break
                        else:
                            self.lista[i + 1] = tk.PhotoImage(file=result[i + 1][2])
                            break

            print(self.lista)
        except Exception as erro:
            print("Novo erro: ", erro)

        try:
            if self.lista[0]:
                self.img01.create_image(75, 75, image=self.lista[0])
                self.lb01 = tk.Entry(self)
                self.lb01.grid(column=1, row=2)
                self.lb01.insert(0, result[0][1])

            if self.lista[1]:
                self.img02.create_image(75, 75, image=self.lista[1])
                self.lb02 = tk.Entry(self)
                self.lb02.grid(column=2, row=2)
                self.lb02.insert(0, result[1][1])

            if self.lista[2]:
                self.img03.create_image(75, 75, image=self.lista[2])
                self.lb03 = tk.Entry(self)
                self.lb03.grid(column=3, row=2)
                self.lb03.insert(0, result[2][1])

            if self.lista[3]:
                self.img04.create_image(75, 75, image=self.lista[3])
                self.lb04 = tk.Entry(self)
                self.lb04.grid(column=1, row=4)
                self.lb04.insert(0, result[3][1])

            if self.lista[4]:
                self.img05.create_image(75, 75, image=self.lista[4])
                self.lb05 = tk.Entry(self)
                self.lb05.grid(column=2, row=4)
                self.lb05.insert(0, result[4][1])

            if self.lista[5]:
                self.img06.create_image(75, 75, image=self.lista[5])
                self.lb06 = tk.Entry(self)
                self.lb06.grid(column=3, row=4)
                self.lb06.insert(0, result[5][1])

            if self.lista[6]:
                self.img07.create_image(75, 75, image=self.lista[6])
                self.lb07 = tk.Entry(self)
                self.lb07.grid(column=1, row=6)
                self.lb07.insert(0, result[6][1])

            if self.lista[7]:
                self.img08.create_image(75, 75, image=self.lista[7])
                self.lb08 = tk.Entry(self)
                self.lb08.grid(column=2, row=6)
                self.lb08.insert(0, result[7][1])

            if self.lista[8]:
                self.img09.create_image(75, 75, image=self.lista[8])
                self.lb09 = tk.Entry(self)
                self.lb09.grid(column=3, row=6)
                self.lb09.insert(0, result[8][1])

        except Exception as erro:
            print(erro)

        self.sair = tk.Button(self, text="Sair",
                              command=lambda: master.trocar_tela(Login))
        self.btn_adicionar = tk.Button(self, text="Adicionar", command=lambda: self.adicionar(master))
        self.btn_atualizar = tk.Button(self, text="Registrar nomes", command=lambda: self.atualizar_nomes())

        self.tela.grid(column=2, row=0)
        self.img01.grid(column=1, row=1)
        self.img02.grid(column=2, row=1)
        self.img03.grid(column=3, row=1)
        self.img04.grid(column=1, row=3)
        self.img05.grid(column=2, row=3)
        self.img06.grid(column=3, row=3)
        self.img07.grid(column=1, row=5)
        self.img08.grid(column=2, row=5)
        self.img09.grid(column=3, row=5)

        self.btn_adicionar.grid(column=2, row=7)
        self.btn_atualizar.grid(column=2, row=8)
        self.sair.grid(column=2, row=9)

    def adicionar(self, master):
        try:
            user = usuario_sessao
            path = tk.filedialog.askopenfilenames()
            for i in range(len(path)):
                arquivo = ntpath.basename(path[i])
                bd.bd.insert_image(self, user, f'img{i}', path[i], arquivo)
            master.trocar_tela(Principal)
            print("Cadastro feito com sucesso")
        except Exception as erro:
            print(erro)

    def atualizar_nomes(self):
        try:
            if self.lb01:
                self.lb01.get()
                bd.bd.update_title(self, self.lb01.get(), self.caminho[0][2], usuario_sessao)
            if self.lb02:
                self.lb02.get()
                bd.bd.update_title(self, self.lb02.get(), self.caminho[1][2], usuario_sessao)
            if self.lb03:
                self.lb03.get()
                bd.bd.update_title(self, self.lb03.get(), self.caminho[2][2], usuario_sessao)
            if self.lb04:
                self.lb04.get()
                bd.bd.update_title(self, self.lb04.get(), self.caminho[3][2], usuario_sessao)
            if self.lb05:
                self.lb05.get()
                bd.bd.update_title(self, self.lb05.get(), self.caminho[4][2], usuario_sessao)
            if self.lb06:
                self.lb06.get()
                bd.bd.update_title(self, self.lb06.get(), self.caminho[5][2], usuario_sessao)
            if self.lb07:
                self.lb07.get()
                bd.bd.update_title(self, self.lb07.get(), self.caminho[6][2], usuario_sessao)
            if self.lb08:
                self.lb08.get()
                bd.bd.update_title(self, self.lb08.get(), self.caminho[7][2], usuario_sessao)
            if self.lb09:
                self.lb09.get()
                bd.bd.update_title(self, self.lb09.get(), self.caminho[8][2], usuario_sessao)
        except Exception as erro:
            print(erro)

    def deletar_imagem(self, master, path, user, title):
        bd.bd.delete_image(self, user, title, path)
        master.trocar_tela(Principal)


if __name__ == "__main__":
    app = App()
    app.geometry("800x640")
    app.mainloop()
