from model import dbase
def update(id, qt):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = f"""UPDATE Produto SET qt={qt} WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as n:
        print(n)
    finally:
        conn.close()
def updateM(id, qt):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = f"""UPDATE Produto SET qt=qt+{qt} WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as x:
        print(x)
    finally:
        conn.close()

def storage(id, qt):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = f"""UPDATE Produto SET saida=saida+{qt} WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as z:
        print(z)
    finally:
        conn.close()
    
