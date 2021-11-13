import tkinter as tk

import bd


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("App")
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
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Criando os componentes da tela login
        tk.Label(self, text="Login")
        self.login = tk.Label(self, text="Login").pack()
        self.txt_login = tk.Entry(self).pack()
        self.pwd = tk.Label(self, text="Senha").pack()
        self.txt_pwd = tk.Entry(self).pack()
        self.cadastro = tk.Button(self, text="Cadastro",
                                  command=lambda: master.trocar_tela(Cadastro)).pack()
        self.entrar = tk.Button(self, text="Entrar",
                                command=lambda: master.trocar_tela(Principal)).pack()


class Cadastro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Criando os componetes da tela cadastro
        self.titulo = tk.Label(self, text="Cadastro").pack()
        self.lb_name = tk.Label(self, text="Nome").pack()
        name = self.txt_name = tk.Entry(self).pack()
        self.lb_cpf = tk.Label(self, text="Cpf").pack()
        cpf = self.txt_cpf = tk.Entry(self).pack()
        self.lb_user = tk.Label(self, text="Usuario").pack()
        user = self.txt_user = tk.Entry(self).pack()
        self.lb_pwd = tk.Label(self, text="Senha").pack()
        pwd = self.txt_pwd = tk.Entry(self).pack()
        self.cadastro = tk.Button(self, text="Cadastrar",
                                  command=bd.bd.insert_user(self, name, cpf, user, pwd)).pack()
        self.voltar = tk.Button(self, text="Voltar",
                                command=lambda: master.trocar_tela(Login)).pack()


class Principal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tela = tk.Label(self, text="Tela principal")
        self.sair = tk.Button(self, text="Sair",
                              command=lambda: master.trocar_tela(Login))
        self.adicionar = tk.Button(self, text="Adicionar")

        self.tela.pack()
        self.adicionar.pack()
        self.sair.pack()


if __name__ == "__main__":
    app = App()
    app.geometry("800x640")
    app.mainloop()
