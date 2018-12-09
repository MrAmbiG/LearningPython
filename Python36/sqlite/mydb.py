import sqlite3

conn = sqlite3.connect('comics.db')

c = conn.cursor()
# c.execute ('''
#     CREATE TABLE superhero(
#         name TEXT PRIMARY KEY,
#         power TEXT,
#         publisher TEXT
#     )
# ''')

# c.execute("insert into superhero values('batman', 'rich', 'dc')")
c.execute("insert into superhero values('batman', 'rich', 'dc')") # we should an error for this
c.execute("SELECT * FROM superhero")
print(c.fetchall())
conn.commit()
conn.close()
