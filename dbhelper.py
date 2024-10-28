import sqlite3

database:str = "studentdb.db"

def connect():
    return sqlite3.connect(database)

def getprocess(sql:str)->list:
    conn = connect()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def doprocess(sql:str)->bool:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    return True if cursor.rowcount>0 else False

def deleterecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}` = '{vals[0]}'"
    return doprocess(sql)


def addrecord(table:str,**kwargs)->bool:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    flds:str = "`,`".join(keys)
    data:str = "','".join(vals)
    sql:str = f"INSERT INTO `{table}`(`{flds}`) VALUES ('{data}')"
    print(sql)
    return doprocess(sql)

def getall(table)->list:
    sql:str = f"SELECT * FROM `{table}`" 
    return getprocess(sql)

def editrecord(table, idno, **kwargs)->bool:
    keys = list (kwargs.keys())
    vals = list(kwargs.values())
    set_clause = ",".join([f"`{key}`='{val}'" for key, val in zip(keys, vals)])
    sql = f"UPDATE `{table}` SET {set_clause} WHERE `idno`={idno}"
    return doprocess(sql)