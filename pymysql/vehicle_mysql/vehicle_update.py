from mysql import connector
connection=connector.connect(
           host="localhost",
           user="root",
           password="",
           database="vehicle_db"
)
cursor=connection.cursor()
query=" update vehicles set place=%s where id=%s"
data=("palakkad",2)
cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("table updated..")