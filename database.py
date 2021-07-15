import sqlite3
#table name is quiz_data username text, password text, correct 0, incorrect 0, Avg 0,

conn = sqlite3.connect("data.db")
c = conn.cursor()
def createAccount(username,password):
    print(username,password)
    c.execute(f"""INSERT INTO quiz_data VALUES ('{username}','{password}')""")
    conn.commit()
    c.execute("""SELECT * FROM quiz_data""")
    print(c.fetchall())
def signInAccount(username="",password=""):
    return username, password
c.execute("""SELECT * FROM quiz_data""")
print(c.fetchall())
conn.commit()

#Close our connection
