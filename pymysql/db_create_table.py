from mysql import connector
connection=connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_db"
)
cursor=connection.cursor()
query="""
create table sports(
       id int auto_increment primary key,
       name varchar(200) not null,
       players_count int default 1,
       country varchar(200) not null
)

"""
cursor.execute(query)
connection.commit()

cursor.close()
connection.close()
print("completed")