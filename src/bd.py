import sqlite3


class bd:
    def __init__(self):
        print('Ininciando conexão com o bacno de dados')
        try:
            conection = sqlite3.connect('./bancocadastro.db')
            cursor = conection.cursor()
            print("Conexão com banco feito com sucesso")

        except conection.DatabaseError as erro:
            print("Erro de conexão :", erro)

        finally:
            if conection:
                cursor.close()
                print("tabela fechada")
                conection.close()
                print("Conexão fechada")

    def conection(self):
        try:
            conection = sqlite3.connect('./bancocadastro.db')
            cursor = conection.cursor()
            print("Conexão com banco feito com sucesso")
            ## CRIANDO TABLEA DO USUARIO
            table_pessoa = """CREATE TABLE IF NOT EXISTS pessoa(
                                   nome TEXT NOT NULL,
                                   cpf INT NOT NULL,
                                   user TEXT NOT NULL,
                                   pwd TEXT NOT NULL,
                                   PRIMARY KEY (cpf)
                                   );"""
            ## CRIANDO TABELA IMAGEM
            table_imagem = """CREATE TABLE IF NOT EXISTS imagem(
                                   user TEXT NOT NULL,
                                   title TEXT NOT NULL,
                                   path TEXT NOT NULL,
                                   name TEXT NOT NULL,
                                   FOREIGN KEY (user) REFERENCES pessoa(user)
                                   );"""
            cursor.execute(table_pessoa)
            cursor.execute(table_imagem)
            conection.commit()
            print("tabela criada com sucesso")

        except conection.DatabaseError as erro:
            print("Erro de conexão :", erro)

        finally:
            if conection:
                cursor.close()
                conection.close()
                print("Conexão fechada")

    def insert(self, nome, cpf, user, pwd):
        try:
            conection = sqlite3.connect('./bancocadastro.db')
            cursor = conection.cursor()
            insert = """INSERT INT pessoa(nome,cpf,user,pwd) VALUES(?,?,?,?)"""
            cursor.execute(insert, (nome, cpf, user, pwd))
            conection.commit()
        except conection.DatabaseError as erro:
            print("Erro de conexão : ", erro)
        finally:
            cursor.close()
            conection.close()
