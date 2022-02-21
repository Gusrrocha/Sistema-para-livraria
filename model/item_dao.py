from model import dbase
from model.item import Item

def add(item):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO ItemVenda (nome_produto, quantidade, valor_produto) VALUES (?, ?, ?)"""
        cursor.execute(sql, item.getItem())
        conn.commit()
    except Exception as r:
        print(r)
    finally:
        conn.close()
    
def remove(id):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM ItemVenda WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as o:
        print(o)
    finally:
        conn.close()

def selectRecent():
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT MAX(id) FROM ItemVenda"""
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as u:
        print(u)
    finally:
        conn.close()
    return result

def selectAll():
    li = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM ItemVenda ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            itemm = Item(item[0], item[1], item[2], item[3])
            li.append(itemm)
    except Exception as i:
        print(i)
    finally:
        conn.close()
    return li
def deleteNull():
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM ItemVenda WHERE id_venda is NULL"""
        cursor.execute(sql)
        conn.commit()
    except Exception as d:
        print(d)
    finally:
        conn.close()

def selectAllOne(id):
    lista = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM ItemVenda WHERE id_venda=?"""
        cursor.execute(sql, [id])
        result = cursor.fetchall()
        for item in result:
            no = Item(item[0], None, item[1], item[2], item[3], item[4])
            lista.append(no)
    except Exception as w:
        print(w)
    finally:
        conn.close()
    return lista

def delSNonExistance():
    l = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM ItemVenda"""
        cursor.execute(sql)
        res = cursor.fetchall()
        for i in res:
            n = Item(i[0], None, i[1], i[2],i[3],i[4])
            l.append(n)
        for i in l:
            sql_2 = """SELECT * FROM Venda WHERE id={}""".format(i.id_venda)
            cursor.execute(sql_2)
            r = cursor.fetchall()
            if len(r) != 0:
                pass
            else:
                sql_3 = """DELETE FROM ItemVenda Where id_venda={}""".format(i.id_venda)
                cursor.execute(sql_3)
                conn.commit()
    except Exception as w:
        print(w)
    finally:
        conn.close()