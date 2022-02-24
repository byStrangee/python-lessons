import sqlite3

con = sqlite3.connect('homework.db')

cur = con.cursor()

sql = "CREATE TABLE test()"

cur.execute(sql)
