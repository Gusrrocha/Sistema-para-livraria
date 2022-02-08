from model import dbase
def update(id, qt):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = f"""UPDATE Produto SET qt={qt} WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
        conn.close()
    except Exception as n:
        print(n)
    finally:
        conn.close()