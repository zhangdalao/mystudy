import pymysql

def get_sql(sql):
    host,user,password,database,port,charset = ['127.0.0.1','root','cxy123456','fanwe',3306,'utf8']
    db = pymysql.connect(host = host,user = user)

    cursor = db.cursor()
    #运行sql语句
    cursor.execute(sql)
    #把sql运行的数据保存在data变量
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

