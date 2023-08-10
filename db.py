import sqlite3
sqliteConnection = sqlite3.connect('sql.db')

cursor = sqliteConnection.cursor()
a = cursor.execute("select * from scam;")
for row in a:
    print(row)
