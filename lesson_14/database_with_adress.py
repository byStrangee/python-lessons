import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

# cur.execute("CREATE TABLE person(name TEXT, surname TEXT,age TEXT)")


def add(name, surname, age):
    n = "name"
    s = 'surname'
    a = 15
    ad = "Massachutes"
    f = f"INSERT INTO person VALUES('{n}', '{s}', '{a}', '{ad}')"
    cur.execute(f)


def show():
    for i in cur.execute('SELECT * FROM person'):
        print(i)


con.commit()
cur.close()
