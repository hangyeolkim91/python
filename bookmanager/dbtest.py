import sqlite3

conn = sqlite3.connect('blist')
cursor = conn.cursor()
query = "SELECT * FROM booklist WHERE bname='{0}' OR aname='{1}'".format('aa','')
cursor.execute(query)
print(str(cursor.fetchall()))