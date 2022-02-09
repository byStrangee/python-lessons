import sqlite3
import random
con = sqlite3.connect("person.db")

          

def add(name, age):
      sqlCode = f"""\
      INSERT INTO me(name, age) 
            VALUES('{name}', '{age}')
      """
      cur.execute(sqlCode)


def get(tableName):
      l = []
      sqlCode = f"""\
            SELECT * FROM {tableName}
      """
      for i in cur.execute(sqlCode):
            l.append(i)
      return l


add('john doe', '45')

print(get('me+'))

con.commit()