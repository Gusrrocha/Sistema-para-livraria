from model import dbase
def add(venda):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Venda (cliente, funcionario, valor) VALUES (?, ?, ?)"""
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