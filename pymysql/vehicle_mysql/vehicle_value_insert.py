from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vehicle_db"
)##vehicle(id,name,model,running_km,fuel_type,owner_type,place,owner)
cursor=connection.cursor()
query="""
insert into vehicles(name,model,running_km,fuel_type,owner_type,place,owner)values(%s,%s,%s,%s,%s,%s,%s)
"""

data=('i20', '2021', 15000, 'Petrol', 'First', 'Trivandrum', 'Nikhil')
cursor.execute(query,data)
connection.commit()
cursor.close()
connection.close()
print("values inserted..")