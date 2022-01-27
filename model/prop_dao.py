from model import dbase
from model.produto import Produto

def addProd(produto):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Produto (nome, qt, valor, valor_compra) VALUES (?,?,?,?)"""
        cursor.execute(sql, produto.getProd())
        conn.commit()
    except Exception as i:
        print(i)
    finally:
        conn.close()

def editProd(produto):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Produto SET nome=?, qt=?, valor=?, valor_compra=? WHERE id=?"""
        cursor.execute(sql, produto.id)
        conn.commit()
    except Exception as a:
        print(a)
    finally:
        conn.close()
    
def selectAll():
    l_p = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Produto ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for prod in result:
            new = Produto(prod[0], prod[1], prod[2], prod[3], prod[4])
            l_p.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return l_p
