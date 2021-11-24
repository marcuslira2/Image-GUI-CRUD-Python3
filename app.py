import ntpath
import os.path

import sqlite3
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog as fd

usuario_sessao = ''

"""Criando janela principal do programa"""
janela = tk.Tk()
janela.title("App")
janela.geometry('840x640')
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)
"""Criando os Frames"""
f0 = tk.Frame(janela)
f1 = tk.Frame(janela)
f2 = tk.Frame(janela)
f3 = tk.Frame(janela)

"""Funções"""

"""Trocar de tela"""


def swap(frame):
    frame.tkraise()


for frame in (f1, f2, f3):
    frame.grid(column=0, row=0, stick='nsew')


def visualizar():
    try:
        usuario = usuario_sessao
        connection = sqlite3.connect('./bancocadastro.db')
        cursor = connection.cursor()
        select = """SELECT * FROM imagem WHERE user =?"""
        cursor.execute(select, [usuario])
        result = cursor.fetchall()
        for item in result:
            print(item[2])
            normal =os.path.normpath(item[2])
            print(normal)


    except Exception as erro:
        print(erro)
    finally:
        if connection:
            cursor.close()
            connection.close()

    # filepath = result[0][2]
    # print(filepath)
    # lista = {}
    # print(len(lista))
    # lista[0] = tk.PhotoImage(file=filepath)
    # print(lista[0])
    #
    # img01.create_image(100, 100, image=lista[0])


"""FRAME 1 LOGIN"""

lb1 = tk.Label(f1, text='Tela de Login')
lb1.pack()

lb_user = tk.Label(f1, text="Login")
lb_user.pack()

txt_login_usuario = tk.Entry(f1)
txt_login_usuario.pack()

lb_pwd = tk.Label(f1, text="Senha")
lb_pwd.pack()

txt_login_pwd = tk.Entry(f1)
txt_login_pwd.pack()

btn_entrar = tk.Button(f1, text='Login', command=lambda: [verificar(), visualizar()])
btn_entrar.pack()
btn_cadastro = tk.Button(f1, text='Cadastro', command=lambda: swap(f2))
btn_cadastro.pack()

tentativas = 0

"""FUNÇÕES FRAME1 LOGGIN"""


def verificar():
    global tentativas
    try:
        user = txt_login_usuario.get()
        pwd = txt_login_pwd.get()
        connection = sqlite3.connect('./bancocadastro.db')
        cursor = connection.cursor()
        select = """SELECT * FROM pessoa WHERE user = ?"""
        cursor.execute(select, [user])
        result = cursor.fetchone()
        print(result)
        if user in result[2] and pwd in result[3]:
            global usuario_sessao
            usuario_sessao = user
            print(usuario_sessao)
            swap(f3)
            tentativas = 0
        elif user in result[2] and pwd not in result[3]:
            tentativas += 1
            if tentativas < 5:
                tk.messagebox.showinfo("Alert",
                                       f"Senha errada, tente novametne, numero de tentativas restantes {5 - tentativas}")
            elif tentativas >= 5:
                txt_user.get()
                tk.messagebox.showinfo("Alert", "Usuario bloqueado por 1 minuto")
                tentativas = 0
            else:
                print('erro')
        else:
            print("Usuario não cadastrado")
    except Exception as erro:
        print("Erro ao pequisar usuario : ", erro)

    finally:
        if connection:
            cursor.close()
            connection.close()


"""FRAME 2 CADASTRO"""
titulo = tk.Label(f2, text='Cadastrar')
titulo.pack()
lb_name = tk.Label(f2, text="Nome").pack()
txt_name = tk.Entry(f2)
txt_name.pack()
lb_cpf = tk.Label(f2, text="Cpf").pack()
txt_cpf = tk.Entry(f2)
txt_cpf.pack()
lb_user = tk.Label(f2, text="Usuario").pack()
txt_user = tk.Entry(f2)
txt_user.pack()
lb_pwd = tk.Label(f2, text="Senha").pack()
txt_pwd = tk.Entry(f2)
txt_pwd.pack()

btn_cadastrar = tk.Button(f2, text='Cadastrar', command=lambda: [cadastrar_pessoa(), msgbox(),
                                                                 swap(f1)])
btn_cadastrar.pack()
btn_sair = tk.Button(f2, text='Sair', command=lambda: swap(f1))
btn_sair.pack()

"""Funcções FRAME 2 CADASTRO"""


def msgbox():
    tk.messagebox.showinfo("Sucess", "Usuario cadastrado com sucesso")


def cadastrar_pessoa():
    try:
        name = txt_name.get()
        cpf = txt_cpf.get()
        user = txt_user.get()
        pwd = txt_pwd.get()
        connection = sqlite3.connect('./bancocadastro.db')
        cursor = connection.cursor()
        insert = """INSERT INTO pessoa(nome,cpf,user,pwd) VALUES(?,?,?,?)"""
        registro = (name, cpf, user, pwd)
        cursor.execute(insert, registro)
        connection.commit()
        print("Cadastro realizado com sucesso")
    except Exception as erro:
        print("não foi possivel fazer o cadastro: ", erro)
    finally:
        if connection:
            cursor.close()
            connection.close()


"""FRAME 3 VISUALIZAÇÃO"""
lb3 = tk.Label(f3, text='Visualização')
lb3.grid(row=0, column=2)

"""Canvas FRAME 3 VISUALIZAÇÃO"""

img01 = tk.Canvas(f3, width=150, height=150, bg='red')
img01.grid(column=1, row=1)
imagem2 = tk.PhotoImage(file='C:/Users/CLEIDE_PC/Pictures/Pokemon/32px-Pokémon_Fire_Type_Icon.svg.png')
img01.create_image(75, 75, image=imagem2)

img02 = tk.Canvas(f3, width=150, height=150, bg='red')
img02.grid(column=2, row=1)
img03 = tk.Canvas(f3, width=150, height=150, bg='red')
img03.grid(column=3, row=1)
img04 = tk.Canvas(f3, width=150, height=150, bg='red')
img04.grid(column=1, row=2)
img05 = tk.Canvas(f3, width=150, height=150, bg='red')
img05.grid(column=2, row=2)
img06 = tk.Canvas(f3, width=150, height=150, bg='red')
img06.grid(column=3, row=2)
img07 = tk.Canvas(f3, width=150, height=150, bg='red')
img07.grid(column=1, row=3)
img08 = tk.Canvas(f3, width=150, height=150, bg='red')
img08.grid(column=2, row=3)
img09 = tk.Canvas(f3, width=150, height=150, bg='red')
img09.grid(column=3, row=3)

"""Botões FRAME 3 VISUALIZAÇÕES"""
btn_backward = tk.Button(f3, text='voltar')
btn_backward.grid(column=0, row=2)

btn_forward = tk.Button(f3, text='avançar')
btn_forward.grid(column=4, row=2)

btn_adicionar = tk.Button(f3, text='Adicionar', command=lambda: adicionar())
btn_adicionar.grid(column=2, row=7)

btn_atualizar = tk.Button(f3, text='Atualizar', command=lambda: visualizar())
btn_atualizar.grid(column=2, row=8)

btn_fechar = tk.Button(f3, text="Sair", command=lambda: swap(f1))
btn_fechar.grid(column=2, row=9)

"""Funções FRAME 3 VISUALIZAÇÃO"""


def adicionar():
    try:
        nome_cadastro = usuario_sessao
        caminho = tk.filedialog.askopenfilenames()
        for i in range(len(caminho)):
            arquivo = ntpath.basename((caminho[i]))
            try:

                connection = sqlite3.connect('./bancocadastro.db')
                cursor = connection.cursor()
                insert = """INSERT INTO imagem(user,title,path,name) VALUES(?,?,?,?)"""
                cursor.execute(insert, (nome_cadastro, f'img{i}', caminho[i], arquivo))
                connection.commit()
                print('imagem cadastrado com sucesso!')
            except Exception as erro:
                print(erro)
            finally:
                if connection:
                    cursor.close()
                    connection.close()


    except Exception as erro:
        print(erro)


"""INICIAR O PROGRAMA"""
swap(f1)
janela.mainloop()
