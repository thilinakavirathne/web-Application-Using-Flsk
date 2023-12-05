import sqlite3

connection = sqlite3.connect('database.db')

# Read and execute schema.sql to create tables
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insert sample posts
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post'))

# Insert sample users
cur.execute("INSERT INTO users (username, Ppassword) VALUES (?, ?)",
            ('user1', ' '))

cur.execute("INSERT INTO users (username, Ppassword) VALUES (?, ?)",
            ('user2', 'securepass'))

connection.commit()
connection.close()
