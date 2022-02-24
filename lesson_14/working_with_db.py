# SQL - Structured Query Language
import sqlite3


#  It creates a new database.db if "database.db" not exist or else it connects automatically
con = sqlite3.connect('database.db')


# It makes a new cursor to work with it
cur = con.cursor()


# executor = """
#     CREATE TABLE database(
#         song_link TEXT,
#         song_views INTEGER PRIMARY KEY AUTOINCREMENT,
#         son_author TEXT
#     )
# """

# executor = "INSERT INTO database VALUES('https://open.spotify.com/track/asafa68rf478a64d', 29000, 'NEFFEX')"

# adds a new values for databases table
def add(song_link, song_views, song_author):
    try:
        command = f"INSERT INTO database VALUES('{song_link}', {(song_views)}, '{song_author}')"
        cur.execute(command)
    except sqlite3.DatabaseError as warn:
        print(warn)
    else:
        print('succesfully added')


def show():
    try:
        command = "SELECT s FROM database"
        for i in cur.execute(command):
            print(i)
    except sqlite3.DatabaseError as me:
        print(me)
    else:
        print("-----------END-----------")


print('Give me 3 values for my database')
print("second one must be int !!!")
_link = input('song link :  ')
_views = input('song views :  ')
_author = input('song author : ')
add(_link, _views, _author)
print('-----------START-----------')
show()
con.commit()
cur.close()
