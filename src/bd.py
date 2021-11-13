import sqlite3


class bd:
    def __init__(self):
        print('Ininciando conexão com o bacno de dados')

    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('./bancocadastro.db')
            cursor = self.connection.cursor()
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
            self.connection.commit()
            print("tabela criada com sucesso")

        except ConnectionError as erro:
            print("Erro de conexão :", erro)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("Conexão fechada")

    ## Criação de usuario
    def insert_user(self, nome, cpf, user, pwd):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            insert = """INSERT INTO pessoa(nome,cpf,user,pwd) VALUES(?,?,?,?)"""
            registro = (nome, cpf, user, pwd)
            cursor.execute(insert, registro)
            self.conection.commit()
        except Exception as erro:
            print("Erro ao inserir novo usuario : ", erro)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()

    ## Seleção de usuario
    def select_user(self, user, pwd):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            select = """SELECT * FROM pessoa WHERE user = ? and pwd = ?"""
            cursor.execute(select, (user, pwd))
            if user and pwd in select:
                print("Entrando")
            elif user and not pwd in select:
                print("Senha invalida, Tente novamente")
            else:
                print("Usuario não existente, cadastre um novo usuario")

        except Exception as erro:
            print("Erro ao pequisar usuario : ", erro)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def insert_image(self, user, title, path, name):
        try:
            self.conection()
            cursor = self.conection.cursor()
            insert = """INSERT INTO imagem(user,title,path,name) VALUES(?,?,?,?)"""
            cursor.execute(insert, (user, title, path, name))
            self.conection.commit()
        except Exception as erro:
            print("Erro ao inserir nova imagem : ", erro)
        finally:
            if self.conection:
                cursor.close()
                self.conection.close()

    def select_image(self, user, path):
        try:
            self.conection()
            cursor = self.conection.cursor()
            select = """SELECT * FROM imagem WHERE user =? and path =?"""
            cursor.execute(select, (user, path))
        except Exception as erro:
            print("Erro ao selecionar imagem: ", erro)
        finally:
            if self.conection:
                cursor.close()
                self.conection.close()

    def update_image(self, title, path):
        try:
            self.conection()
            cursor = self.conection.cursor()
            update = """UPDATE imagem SET title = ? and path=?"""
            cursor.execute(update, (title, path))
            self.conection.commit()
        except Exception as erro:
            print("Erro ao atualizar imagem :", erro)
        finally:
            if self.conection:
                cursor.close()
                self.conection.close()

    def delete_image(self, title, path):
        try:
            self.conection()
            cursor = self.conection.cursor()
            delete = """DELETE FROM imagem WHERE title = ? and path=?"""
            cursor.execute(delete, (title, path))
            self.conection.commit()
        except Exception as erro:
            print("Erro ao deletar imagem :", erro)

        finally:
            cursor.close()
            self.conection.close()

    def initial_image(self, user):
        try:
            self.conection()
            cursor = self.conection.cursor()
            select = """SELECT * FROM imagem WHERE user =?"""
            cursor.execute(select, (user))
            cursor.fetchall()
        except Exception as erro:
            print("Erro ao selecionar imagem: ", erro)
        finally:
            if self.conection:
                cursor.close()
                self.conection.close()
