from mysql import connector
connection=connector.connect(
           host="localhost",
           user="root",
           password="",
           database="vehicle_db"
           
)
cursor=connection.cursor()
query="""
select * from vehicles
"""
cursor.execute(query)
records=cursor.fetchall()
for row in records:
    print(row)
cursor.close()
connection.close()
