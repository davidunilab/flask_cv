import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

''
""
"""  """
students = [
    ["Giorgi Tchanturia", 14],
    ["Lasha Tsveraidze", 22],
    ["Anna Tskhakaia", 22],
]


# cur.execute("""
#     insert into students (name, age) values (?, ?)
#     """, ("Giorgi Tchanturia", 15))


# for i in students:
#     name = i[0]
#     age = i[1]

#     cur.execute("""
#     insert into students (name, age) values (?, ?)
#     """, (name, age))
#     con.commit() # save

# cur.executemany("""insert into students (name, age) values (?, ?) """, students)
# con.commit()

# cur.execute(""" update students set age=?, name=? where name = ?""", (15,"გიორგი ჭანტურია", "Giorgi Tchanturia"))
# con.commit()and ჭანტურია",))
# con.commit()


q = cur.execute(""" select count(*) from students where age = 22 """)

print( q.fetchall() )


con.close()

