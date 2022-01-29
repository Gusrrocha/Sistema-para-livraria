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