
import sqlite3 as sql
import os

veritabani = 'ülkelerimiz.db'
dosya_mevcut = os.path.exists(veritabani)

vt = sql.connect('ülkelerimiz.db')
imleç = vt.cursor()

#table = imleç.execute('CREATE TABLE IF NOT EXISTS ülkebilgileri (başkent text, iklim text, parabirimi text, nüfus integer)')

#veri_girişi = ('''INSERT INTO ülkebilgileri VALUES ('bogota', 'tropikal iklimi', 'peso', 52000000)''')

#imleç.execute(veri_girişi)

imleç.execute('SELECT * FROM ülkebilgileri')
bilgiler = imleç.fetchall()
#print(bilgiler[0])

a = 1
for i in bilgiler:
    print(a, end=' ')
    for k in i:
       print(k, end=' ')
    print('')
    a += 1

vt.commit()

#imleç.execute('''UPDATE ülkebilgileri SET başkent = 'washington' WHERE iklim = 'tropikal iklimi' ''')
#vt.commit()

#imleç.execute('''DELETE FROM ülkebilgileri WHERE nüfus = '52000000' ''')
#vt.commit()




vt.close()