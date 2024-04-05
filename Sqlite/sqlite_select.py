
import sqlite3 as sql

# tablodan veri çekme -> SELECT * FROM tablo ismi
# tablodan veri çekme -> SELECT col1, col2, col3 ..... FROM tablo ismi
# tablodan veri çekme -> SELECT col1, col2, col3.... FROM tablo ismi WHERE col1 : val1...

con = sql.connect('öğretmen.db')
cur = con.cursor()

cur.execute('''SELECT * FROM özellikler WHERE maaş > ('50000')''')
data = cur.fetchall()

print(type(data))
print('*****************')
print(data)
print('*****************')

for line in data:
    print(type(line))
    print(line)