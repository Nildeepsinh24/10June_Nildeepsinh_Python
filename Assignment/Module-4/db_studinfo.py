import sqlite3

try:
    con=sqlite3.connect("studinfo.db")
    print("Database Created/Connected!")
except Exception as e:
    print(e)

#table created
tbl_created="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    con.execute(tbl_created)
    print("Table Created")
except Exception as e:
    print(e)

#INSERT
"""insert_data="insert into studinfo(name,city)values('A','rajkot'),('B','Ahmedabad'),('C','Surat'),('D','Jamnagar')"
try:
    con.execute(insert_data)
    con.commit()
    print("record inserted!")
except Exception as e:
    print(e)"""

"""#Update
update_data="update studinfo set city = 'junagadh' where id=4"
try:
    con.execute(update_data)
    con.commit()
    print("record updated!")
except Exception as e:
    print(e)"""

#Delete
delete_data="delete from studinfo where id = 8"
try:
    con.execute(delete_data)
    con.commit()
    print("record deleted!")
except Exception as e:
    print(e)