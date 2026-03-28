from mysql import connector
connection=connector.connect(
           host="localhost",
           user="root",
           password=""

           
)
print(connection)
cursor=connection.cursor()
query="create database vehicle_db"
cursor.execute(query)
connection.commit()
print("completed")
