from mysql import connector
connection=connector.connect(
          host="localhost",
          user="root",
          password="",
          database="py_db"

)
cursor=connection.cursor()
query="update sports set country =%s where id=%s"
data=("australia",4)
cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("updated...")