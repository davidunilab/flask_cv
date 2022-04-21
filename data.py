import sqlite3

working = [
        {
            "from":2021,
            "to":2022,
            "position":"Back End Developer",
        },        {
            "from":2019,
            "to":2021,
            "position":"Back End Developer",
        },        {
            "from":2021,
            "to":2022,
            "position":"Back End Developer",
        },        {
            "from":2021,
            "to":2022,
            "position":"Back End Developer",
        },        {
            "from":2021,
            "to":2022,
            "position":"Back End Developer",
        },
        
        ]

con = sqlite3.connect('cv.db')
cur = con.cursor()

cur.execute("""
    create table work (
        start TEXT,
        finish TEXT,
        position TEXT,
        description TEXT
    )
""")

con.commit()


for i in working:
    cur.execute(""" insert into work (start, finish, position) values (?,?,?)""", 
    (i.get('from'), i.get('to'), i.get('position')  ))
    con.commit()

con.close()