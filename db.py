import  sqlite3
conn = sqlite3.connect("students.sqlite")
curr = conn.cursor()

sql_query = """ CREATE TABLE student (id integer PRIMARY KEY,
            name varchar(70) NOT NULL,
            branch varchar(50) NOT NULL )
            """

curr.execute(sql_query)