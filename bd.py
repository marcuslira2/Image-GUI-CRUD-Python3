import sqlite3


class bd:
    def __init__(self):
        print('Ininciando conexão com o bacno de dados')

    def abrirConexao(self):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
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
            connection.commit()
            print("tabela criada com sucesso")

        except sqlite3.DatabaseError as erro:
            print("Erro de conexão :", erro)

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Conexão fechada")

    ## Criação de usuario
    def insert_user(self, nome, cpf, user, pwd):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            insert = """INSERT INTO pessoa(nome,cpf,user,pwd) VALUES(?,?,?,?)"""
            registro = (nome, cpf, user, pwd)
            cursor.execute(insert, registro)
            connection.commit()
        except Exception as erro:
            print("Erro ao inserir novo usuario : ", erro)
        finally:
            if connection:
                cursor.close()
                connection.close()

    ## Seleção de usuario
    def select_user(self, user):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            select = """SELECT * FROM pessoa WHERE user = ?"""
            cursor.execute(select, [user])
            result = cursor.fetchone()
            print(result)
            return result

        except Exception as erro:
            print("Erro ao pequisar usuario : ", erro)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def insert_image(self, user, title, path, name):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            insert = """INSERT INTO imagem(user,title,path,name) VALUES(?,?,?,?)"""
            cursor.execute(insert, (user, title, path, name))
            connection.commit()
            return title, path, name

        except Exception as erro:
            print("Erro ao inserir nova imagem : ", erro)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def select_image(self, user, path):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            select = """SELECT * FROM imagem WHERE user =? and path =?"""
            cursor.execute(select, (user, path))
        except Exception as erro:
            print("Erro ao selecionar imagem: ", erro)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update_image(self, title, path):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            update = """UPDATE imagem SET title = ? and path=?"""
            cursor.execute(update, (title, path))
            connection.commit()
        except Exception as erro:
            print("Erro ao atualizar imagem :", erro)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_image(self, title, path):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            delete = """DELETE FROM imagem WHERE title = ? and path=?"""
            cursor.execute(delete, (title, path))
            connection.commit()
        except Exception as erro:
            print("Erro ao deletar imagem :", erro)

        finally:
            cursor.close()
            connection.close()

    def initial_image(self, user):
        try:
            connection = sqlite3.connect('./bancocadastro.db')
            cursor = connection.cursor()
            select = """SELECT * FROM imagem WHERE user =?"""
            cursor.execute(select, (user))
            cursor.fetchall()
        except Exception as erro:
            print("Erro ao selecionar imagem: ", erro)
        finally:
            if connection:
                cursor.close()
                connection.close()
