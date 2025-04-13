import sqlite3

conn= sqlite3.connect("lappy.db")
cursor= conn.cursor()

query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query ="INSERT INTO sys_command VALUES (null,'Academics','D:/academics')"
# cursor.execute(query)
# conn.commit()

query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query ="UPDATE web_command SET name='gfg' WHERE id=2"
cursor.execute(query)
conn.commit()