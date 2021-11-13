import tkinter as tk


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
        tk.Label(self, text="Login").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Cadastro",
                  command=lambda: master.trocar_tela(Cadastro)).pack()
        tk.Button(self, text="Entrar",
                  command=lambda: master.trocar_tela(Principal)).pack()


class Cadastro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.titulo = tk.Label(master, text="Cadastro")

        self.lb_name = tk.Label(master, text="Nome")
        self.txt_name = tk.Entry()
        self.lb_cpf = tk.Label(master, text="Cpf")
        self.txt_cpf = tk.Entry()
        self.lb_user = tk.Label(master, text="Usuario")
        self.txt_user = tk.Entry()
        self.lb_pwd = tk.Label(master, text="Senha")
        self.txt_pwd = tk.Entry()

        self.cadastro = tk.Button(self, text="Cadastrar",
                                  command=lambda: master.trocar_tela(Login))
        self.voltar = tk.Button(self, text="Voltar",
                                command=lambda: master.trocar_tela(Login))

        # Posicionando componentes
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


class Principal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tela =tk.Label(master, text="Tela principal")
        self.sair=tk.Button(master, text="Sair",
                  command=lambda: master.trocar_tela(Login))
        self.adicionar=tk.Button(master,text="Adicionar")

        self.tela.pack()
        self.adicionar.pack()
        self.sair.pack()


if __name__ == "__main__":
    app = App()
    app.geometry("800x640")
    app.mainloop()
