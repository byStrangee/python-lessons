import sqlite3
import random
con = sqlite3.connect("person.db")

cur = con.cursor()

sql = ''
def add(name, age):
      global sql
      sql = f"""\
      INSERT INTO me(name, age) 
            VALUES('{name}', '{age}')
      """

add("myName", "50")
get = """\
      SELECT * FROM me
"""

for row in cur.execute(get):
      print(row)

cur.execute(sql)
con.commit()