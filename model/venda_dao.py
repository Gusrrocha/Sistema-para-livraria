from model import dbase
from model.venda import Venda
def add(venda):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Venda (cliente, funcionario, valor, data) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, venda.getSale())
        conn.commit()
    except Exception as p:
        print(p)
    finally:
        conn.close()
    
def selectRecent():
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT MAX(id) FROM Venda"""
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as g:
        print(g)
    finally:
        conn.close()
    return result

def selectAll():
    list = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Venda ORDER BY id DESC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for v in result:
            novo = Venda(v[0], v[1], v[2], v[3], v[4])
            list.append(novo)
    except Exception as k:
        print(k)
    finally:
        conn.close()
    return list

def deletePastMonth():
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Venda WHERE data <= date('now', 'LocalTime', '-1 month')"""
        cursor.execute(sql)
        conn.commit()
    except Exception as m:
        print(m)
    finally:
        conn.close()
