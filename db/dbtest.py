import sqlite3

conn = sqlite3.connect("friends.db")

cursor = conn.cursor()




query = '''CREATE TABLE myfriends (
    name VARCHAR(20),
    age INT(2),
    sex CHAR(2),
    birth DATE,
    death DATE)'''


data = {'name':'아이유','age':23,'sex':'F','birth':'1993-02-07','death':'NULL'}

query1 = "INSERT INTO myfriends VALUES ('{name}',{age},'{sex}','{birth}','{death}')".format_map(data)

#query = "INSERT INTO pets VALUES ('누룽이', '노선화', '고양이', '암컷', '1993-02-04', NULL)"

print(query1)

cursor.execute(query1)
conn.commit()


cursor.execute('select * from myfriends')

for rec in cursor.fetchall():
    print(rec)





