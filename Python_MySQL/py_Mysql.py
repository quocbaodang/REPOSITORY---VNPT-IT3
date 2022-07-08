import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=QUOCBAODANG;"
                      "Database=student;"
                      "Trusted_Connection=yes;")
 
 
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Info')
 
for row in cursor:
    print('row = %r' % (row,))