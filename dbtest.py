import sqlite3

conn = sqlite3.connect('movies.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE MOVIE (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    TITLE VARCHAR(80) NOT NULL, 
                                    YR INTEGER);''')
print ("Table created successfully")

conn.close()


