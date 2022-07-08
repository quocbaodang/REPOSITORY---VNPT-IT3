import sqlite3

conn = sqlite3.connect('student.db')
# create a cursor object using the cursor method
cursor = conn.cursor()
# create table 
student = """CREATE TABLE IF NOT EXISTS student (NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
cursor.execute(student)


cursor.execute('''INSERT INTO STUDENT VALUES ('Ronaldo', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Messi', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Neymar', '9th', 'C')''')
cursor.execute('''INSERT INTO STUDENT (CLASS, SECTION, NAME) VALUES ('4th', 'A', 'Bao')''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Le', '2th', 'B')''')


print("Data Inserted in the table:")
data = cursor.execute('''SELECT *FROM STUDENT''')
for row in data:
    print(row)
conn.commit()
conn.close()


