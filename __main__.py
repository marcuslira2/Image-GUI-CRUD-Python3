import ntpath
import sqlite3
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog as fd
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
            pwd = self.txt_pwd.get()
            acesso = bd.bd.select_user(self, user)
            if user in acesso[2]:
                try:
                    connection = sqlite3.connect('./bancocadastro.db')
                    cursor = connection.cursor()
                    select = """SELECT ? FROM pessoa WHERE pwd = ?"""
                    cursor.execute(select, [user, pwd])
                    result = cursor.fetchone()
                    print(result)
                    if result == None:
                        self.tentativas += 1
                        if self.tentativas < 5:
                            tk.messagebox.showinfo("Alert",
                                                   f"Senha errada, tente novametne, numero de tentativas restantes {5 - self.tentativas}")
                        if self.tentativas >= 5:
                            self.txt_login.get()
                            tk.messagebox.showinfo("Alert", "Usuario bloqueado por 1 minuto")
                            self.tentativas = 0
                    else:
                        global usuario_sessao
                        usuario_sessao = user
                        print(usuario_sessao)
                        master.trocar_tela(Principal)
                        self.tentativas = 0
                except Exception as erro:
                    print("Erro ao pequisar usuario : ", erro)

                finally:
                    if connection:
                        cursor.close()
                        connection.close()


            else:
                print("Usuario não cadastrado")

        except sqlite3.DataError as erro:
            print("Erro :", erro)


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

        self.lb01 = tk.Label(self, text="img01")
        self.lb02 = tk.Label(self, text="img02")
        self.lb03 = tk.Label(self, text="img03")
        self.lb04 = tk.Label(self, text="img04")
        self.lb05 = tk.Label(self, text="img05")
        self.lb06 = tk.Label(self, text="img06")
        self.lb07 = tk.Label(self, text="img07")
        self.lb08 = tk.Label(self, text="img08")
        self.lb09 = tk.Label(self, text="img09")

        self.img01 = tk.Canvas(self, width=150, heigh=150)
        self.img02 = tk.Canvas(self, width=150, heigh=150)
        self.img03 = tk.Canvas(self, width=150, heigh=150)
        self.img04 = tk.Canvas(self, width=150, heigh=150)
        self.img05 = tk.Canvas(self, width=150, heigh=150)
        self.img06 = tk.Canvas(self, width=150, heigh=150)
        self.img07 = tk.Canvas(self, width=150, heigh=150)
        self.img08 = tk.Canvas(self, width=150, heigh=150)
        self.img09 = tk.Canvas(self, width=150, heigh=150)

        self.sair = tk.Button(self, text="Sair",
                              command=lambda: master.trocar_tela(Login))
        self.btn_adicionar = tk.Button(self, text="Adicionar", command=lambda: self.adicionar())
        self.btn_forward = tk.Button(self, text="Avançar")
        self.btn_backward = tk.Button(self, text="Voltar")

        self.tela.grid(column=2, row=0)
        self.img01.grid(column=1, row=1)
        self.lb01.grid(column=1, row=2)
        self.img02.grid(column=2, row=1)
        self.lb02.grid(column=2, row=2)
        self.img03.grid(column=3, row=1)
        self.lb03.grid(column=3, row=2)
        self.img04.grid(column=1, row=3)
        self.lb04.grid(column=1, row=4)
        self.img05.grid(column=2, row=3)
        self.lb05.grid(column=2, row=4)
        self.img06.grid(column=3, row=3)
        self.lb06.grid(column=3, row=4)
        self.img07.grid(column=1, row=5)
        self.lb07.grid(column=1, row=6)
        self.img08.grid(column=2, row=5)
        self.lb08.grid(column=2, row=6)
        self.img09.grid(column=3, row=5)
        self.lb09.grid(column=3, row=6)

        self.btn_adicionar.grid(column=2, row=7)
        self.btn_backward.grid(column=0, row=3)
        self.btn_forward.grid(column=6, row=3)
        self.sair.grid(column=2, row=8)

        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            select = """SELECT * FROM imagem WHERE user =?"""
            cursor.execute(select, [usuario_sessao])
            result = cursor.fetchall()
            foto = tkinter.PhotoImage(file=result[0][2])
            self.img01.create_image(20, 20, image=foto)

            print(ntpath.basename(result[0][2]))
        except Exception as erro:
            print(erro)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def adicionar(self):
        try:
            user = usuario_sessao
            path = tk.filedialog.askopenfilenames()
            for i in range(len(path)):
                arquivo = ntpath.basename(path[i])
                bd.bd.insert_image(self, user, f'img{i}', path[i], arquivo)
            print("Cadastro feito com sucesso")
        except Exception as erro:
            print(erro)

    # def deletar(self,user,title, path):
    #     user = usuario_sessao
    #     title =
    #     bd.bd.delete_image(self,user,title,path)


if __name__ == "__main__":
    app = App()
    app.geometry("800x640")
    app.mainloop()
