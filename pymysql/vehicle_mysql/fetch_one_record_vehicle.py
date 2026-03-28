from mysql import connector
connection=connector.connect(
           host="localhost",
           user="root",
           password="",
           database="vehicle_db"
)
cursor=connection.cursor()
query="""
select * from vehicles where id=%s
"""
data=(2,)
cursor.execute(query,data)
record=cursor.fetchone()
print(record)
cursor.close()
connection.close()
