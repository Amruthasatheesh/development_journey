from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vehicle_db"

)   ##vehicle(id,name,model,running_km,fuel_type,owner_type,place,owner)
cursor=connection.cursor()
query="""
create table vehicles(
        id int auto_increment primary key,
        name varchar(100) not null,
        model varchar(200),
        running_km int,
        fuel_type varchar(50),
        owner_type varchar(50),
        place varchar(50) not null,
        owner varchar(100) not null

)
"""
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()
print("table created..")