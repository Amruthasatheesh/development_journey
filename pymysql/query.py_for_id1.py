from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_db"
)

cursor=connection.cursor()
query="select * from sports where id=%s"
data=(1,)
cursor.execute(query,data)
record=cursor.fetchone()
print(record)
cursor.close()
connection.close()

