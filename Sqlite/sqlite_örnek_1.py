
import sqlite3 as sql

con = sql.connect('öğrenci.db')

cur = con.cursor()

#cur.execute('CREATE TABLE IF NOT EXISTS bilgiler (isim text, soyisim text, sınıf int, ortalaması int)')


#cur.execute('''INSERT INTO bilgiler VALUES ('orhan', 'akçay', 8, 55)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('sadık', 'dursun', 7, 67)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('mehmet', 'kılınç', 8, 84)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('nurettin', 'taş', 6, 82)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('ali', 'yurdagelen', 6, 33)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('turan', 'aycan', 7, 54)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('kemal', 'yiğit', 6, 65)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('suat', 'tekgöz', 6, 28)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('mustafa', 'candaş', 7, 53)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('alaattin', 'direk', 8, 94)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('harun', 'sorgun', 7, 90)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('güngör', 'petek', 6, 43)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('altan', 'beşerler', 8, 66)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('fahrettin', 'orbay', 8, 80)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('cihan', 'temeloğlu', 7, 39)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('ömer', 'solak', 6, 51)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('ümit', 'sarıbıyık', 6, 47)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('bestami', 'beklanoğlu', 8, 77)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('muratcan', 'akasya', 7, 95)''')
#cur.execute('''INSERT INTO bilgiler VALUES ('ayhan', 'demir', 7, 36)''')


#cur.execute('''SELECT * FROM bilgiler WHERE sınıf < '7' ''')


#cur.execute('''UPDATE bilgiler SET ortalaması = 30 WHERE soyisim = 'habip' ''')


cur.execute('''DELETE FROM bilgiler''')
veri = cur.fetchall()

for i in veri:
    print(i)


con.commit()

con.close()
