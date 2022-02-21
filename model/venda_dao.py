from model import dbase
from model.venda import Venda
from model.item_dao import Item
import model.item_dao as item_dao
def add(venda):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Venda (cliente, funcionario, valor, data, parcela) VALUES (?, ?, ?, ?, ?)"""
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
            novo = Venda(v[0], v[1], v[2], v[3], v[4], v[5])
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
        sql = """DELETE FROM Venda WHERE data <= datetime('now', 'LocalTime', 'start of month')"""
        cursor.execute(sql)
        conn.commit()
    except Exception as m:
        print(m)
    finally:
        conn.close()

# def selectPastMonth():
#     l = []
#     try:
#         conn = dbase.connect()
#         cursor = conn.cursor()
#         sql = """SELECT * From Venda Where data >= datetime('now', 'start of month', 'LocalTime')"""
#         cursor.execute(sql)
#         res = cursor.fetchall()
#         for v in res:
#             n = Venda(v[0],v[1],v[2],v[3],v[4])
#             l.append(n)
#     except Exception as qwert:
#         print(qwert)
#     finally:
#         conn.close()
#     return l
