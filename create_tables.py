import sqlite3

connection = sqlite3.connect('data.db')    # We create the file where we store our data
cursor = connection.cursor()			   # The cursor is used to run the queries

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES ('test',10.99)")




connection.commit()

connection.close() 