
import sqlite3 as sql

# tablo veri güncelleme -> UPDATE tablo ismi SET colx : valx WHERE colx : val1
# tablodan veri silme -> DELETE FROM tablo ismi WHERE colx : valx

con = sql.connect('öğretmen.db')
cur = con.cursor()

#cur.execute('''UPDATE özellikler SET maaş = ('15000') WHERE isim = ('çetin')''')
#con.commit()

cur.execute('DELETE FROM özellikler')
con.commit()

cur.execute('SELECT * FROM özellikler')
data = cur.fetchall()

for line in data:
    print(line)