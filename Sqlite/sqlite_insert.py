
import sqlite3 as sql

# tabloya kayıt atma -> INSERT INTO tablo ismi VALUES (val1, val2, val3.....)

con = sql.connect('öğretmen.db')

cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS özellikler (isim TEXT, soyisim TEXT, maaş INT, branş TEXT)')

#cur.execute('''INSERT INTO özellikler VALUES ('kemal', 'yangaz', 32000, 'ingilizce')''')
#cur.execute('''INSERT INTO özellikler VALUES ('niyazi', 'kolcu', 34000, 'fizik')''')
#cur.execute('''INSERT INTO özellikler VALUES ('sercan', 'soylu', '35000', 'matematik')''')
#cur.execute('''INSERT INTO özellikler VALUES ('fatih', 'cansız', 28000, 'türkçe')''')
#cur.execute('''INSERT INTO özellikler VALUES ('ayhan', 'dönmez', 45000, 'resim')''')
#cur.execute('''insert into özellikler values ('metin', 'erzincanlı', 30000, 'kimya')''')
#cur.execute('''insert into özellikler values ('güngör', 'görkemli', 22000, 'biyoloji')''')
#cur.execute('''insert into özellikler values ('onur', 'dindar', 56000, 'tarih')''')
#cur.execute('''insert into özellikler values ('metin', 'saka', 62000, 'ingilizce')''')
#cur.execute('''insert into özellikler values ('metin', 'doğan', 66000, 'kimya')''')
#cur.execute('''insert into özellikler values ('metin', 'şahin', 70000, 'coğrafya')''')
#cur.execute('''insert into özellikler values ('saffet', 'akgün', 47000, 'ingilizce')''')
cur.execute('''insert into özellikler values ('ismail', 'bayraktar', 83000, 'ingilizce')''')



con.commit()



con.close()