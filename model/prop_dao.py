from model import dbase
from model.produto import Produto

def addProd(produto):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Produto (img, nome, qt, autor, valor, valor_compra, saida) VALUES (?,?,?,?,?,?,0)"""
        cursor.execute(sql, produto.getProd())
        conn.commit()
    except Exception as i:
        print(i)
    finally:
        conn.close()

def removeP(id):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Produto WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as q:
        print(q)
    finally:
        conn.close()
        
def editProd(produto):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Produto SET img=?, nome=?, qt=?, autor=?, valor=?, valor_compra=? WHERE id=?"""
        p = produto.getProd()
        p.append(produto.id)
        cursor.execute(sql, p)
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
            new = Produto(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6])
            l_p.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return l_p

