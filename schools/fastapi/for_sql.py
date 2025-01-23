import pymysql
from base64 import b64encode as enc

def run(sql):
    conn = pymysql.connect(host='175.126.37.21', user='id231', password='pw231', port=13306, db='db231', charset='utf8')
    cursor = conn.cursor()
    res = select(cursor, sql)
    cursor.close()
    conn.close()
    return res

def select(cursor, sql):
    cursor.execute(sql)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    js = dict()
    i = 0
    for row in rows:
        es = dict()
        j = 0
        for col in columns:
            r = row[j]
            if r.__class__.__name__ == 'bytes':
                print(r[:10])
                re = enc(r).decode('utf-8')
            es[col] = r
            j += 1
        js[i] = es
        i += 1
    
    return js

