from get import l_create, host_list
import mysql.connector as sql

db = 'adlist'
conn = sql.connect(user='root', password='123654', database=db)
cursor = conn.cursor()

def db_fill():
    l_create()
    r_count = 0
    for host in host_list:
        cursor.execute("INSERT INTO adlist_main (hosts) VALUES (%s)", (host,))
        conn.commit()
        r_count += 1
    print(str(r_count) + " records processed")

db_fill()

## добавить метрику скорости выполнения
## слишком медленная скорость записи в БД, нужно передаелать логику записи (одним инсёртом)
## добавить автосоздание базы и таблицы если их не существует