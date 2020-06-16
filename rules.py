import requests
import mysql.connector as sql

data = requests.get("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/dnscrypt-proxy/dnscrypt-proxy.blacklist.txt").text
list = data.split("\n")
db = 'adlist'

conn = sql.connect(user='root', password='123654', database=db)
cursor = conn.cursor()

for host in list:
     line = host.strip()
     if not host.startswith("#"):
          cursor.execute("INSERT INTO adlist_main (hosts) VALUES (%s)", (host,))
          conn.commit()

## добавить метрику скорости выполнения
# слишком медленная скорость выполнения инсёрта, нужно передаелать логику добавления (одной строкой)
## добавить автосоздание базы и таблицы если их не существует