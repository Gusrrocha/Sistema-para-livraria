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
        sql = """SELECT * FROM Cliente ORDER BY nome ASC"""
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

def research(tp):
    l = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Cliente where nome LIKE '{}%'""".format(tp)
        cursor.execute(sql)
        res = cursor.fetchall()
        for c in res:
            yes = Cliente(c[0], c[1], c[2], c[3], c[4])
            l.append(yes)
    except Exception as w:
        print(w)
    finally:
        conn.close()
    return l
