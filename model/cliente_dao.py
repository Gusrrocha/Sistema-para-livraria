import sqlite3
from model import dbase
from model.cliente import Cliente

li = []
def add(cliente):
    li.append(cliente)
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Cliente (nome, telefone, endereco, cpf) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, cliente.getCostumer())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def edit(cliente):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Cliente SET nome=?, telefone=?, endereco=?, cpf=? WHERE id=?"""
        l = cliente.getCostumer()
        l.append(cliente.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def removeC(id):
    try:
        conn = dbase.connect()
        cursor = conn.cursor() 
        sql = """DELETE FROM Cliente WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def selectAll():
    lis = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Cliente ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for cliente in result:
            new = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4])
            lis.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lis