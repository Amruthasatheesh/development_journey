from mysql import connector
connection=connector.connect(
           host="localhost",
           user="root",
           password="",
           database="vehicle_db"
)

cursor=connection.cursor()
query="delete from vehicles where id=%s "
data=(3,)
cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("value deleted..")