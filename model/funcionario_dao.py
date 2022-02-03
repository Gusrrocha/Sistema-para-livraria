import sqlite3
from model import dbase
from model.funcionario import Funcionario

def reg(funcionario):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Funcionario (nome_de_usuario, senha, email) 
                VALUES (?, ?, ?)"""
        cursor.execute(sql, funcionario.getWorker())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def log(us, se):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Funcionario WHERE nome_de_usuario= '{}' AND senha= '{}';""".format(us, se)
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return result

def selectOne(user):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Funcionario WHERE nome_de_usuario= '{}';""".format(user)
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as y:
        print(y)
    finally:
        conn.close()
    return result

