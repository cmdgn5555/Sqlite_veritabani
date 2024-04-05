
import sqlite3 as sql

#conn = sql.connect('ders.db')
#print('bağlantı gerçekleştirildi.')
#
#cur = conn.cursor()
#print('cursor oluşturuldu.')


#cur.execute('''CREATE TABLE IF NOT EXISTS students (isim text, soyisim text, yaş int)''')
#print('tablo oluşturuldu.')

#cur.execute('''INSERT INTO students VALUES ('sadık', 'turkuaz', 54)''')


#veriler = [('mithat', 'baş', 15), ('erhan', 'orak', 19), ('ismail', 'cansever', 40), ('koray', 'ercan', 48)]
#komut = '''INSERT INTO students VALUES {}'''
#for veri in veriler:
#    cur.execute(komut.format(veri))
#    print('kayıtlar eklenmeye devam ediyo..')

#veriler = [('sercan', 'kaya', 44), ('fehmi', 'nurol', 55), ('aras', 'kartal', 62), ('şemsi', 'doğan', 66)]
#komut = '''INSERT INTO students VALUES (?,?,?)'''

#cur.executemany(komut, veriler)
#print('eklemeler devam ediyo.')

#conn = sql.connect('ders.db')
#cur = conn.cursor()
#
#veriler = [('kemalettin', 'sancar', 44), ('suat', 'aydın', 58), ('aycan', 'eren', 42)]
#komut = '''INSERT INTO students VALUES (?,?,?)'''
#cur.executemany(komut, veriler)
#
#conn.commit()
#conn.close()

#def ekle(isim, soyisim, yaş):
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    komut_ekle = '''INSERT INTO students VALUES {}'''
#    veri = (isim, soyisim, yaş)
#
#    cur.execute(komut_ekle.format(veri))
#
#    conn.commit()
#    conn.close()
#
#ekle('seyfi', 'güler', 65)

#conn = sql.connect('ders.db')
#cur = conn.cursor()
#
#cur.execute('''DROP TABLE patronlar''')
#print('silme işlemi başarılı...')
#
#conn.commit()
#conn.close()

#def sil_yas(age):
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    sil_komut = '''DELETE FROM students WHERE yaş = {}'''
#    cur.execute(sil_komut.format(age))
#
#    conn.commit()
#    conn.close()
#
#sil_yas(22)

#def sil_isim(name):
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    sil_komut = '''DELETE FROM students WHERE isim = '{}' '''
#    cur.execute(sil_komut.format(name))
#
#    conn.commit()
#    conn.close()
#
#sil_isim('akova')

#def sil_soyisim(surname):
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    sil_komut = '''DELETE FROM students WHERE soyisim = '{}' '''
#    cur.execute(sil_komut.format(surname))
#
#    conn.commit()
#    conn.close()
#
#sil_soyisim('pelikan')

#def sil_isim_soyisim_yas(name, surname, age):
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    sil_komut = '''DELETE FROM students WHERE isim = '{}' or soyisim = '{}' or yaş = {} '''
#    cur.execute(sil_komut.format(name, surname, age))
#
#    conn.commit()
#    conn.close()
#
#sil_isim_soyisim_yas('hayrettin', 'şen', 21)

#conn = sql.connect('ders.db')
#cur = conn.cursor()

#cur.execute('''SELECT * FROM students''')
#list_all = cur.fetchone()
#list_all2 = cur.fetchone()
#list_all3 = cur.fetchone()
#list_all4 = cur.fetchall()

#many= cur.fetchmany(0)
#print(many)



#print(list_all)
#print(list_all2)
#print(list_all3)
#print(list_all4)

#def print_all():
#    conn = sql.connect('ders.db')
#    cur = conn.cursor()
#
#    cur.execute(''' SELECT * FROM students ''')
#    list_all = cur.fetchall()
#
#    for i in list_all:
#        print(i)
#
#    conn.commit()
#    conn.close()
#
#print_all()

#conn = sql.connect('ders.db')
#cur = conn.cursor()
#
##cur.execute('''CREATE TABLE calısanlar (id int PRIMARY KEY, ad text, soyad text, maas int) ''')
#
##veriler = [('ali', 'çapanoğlu', 12000), ('necdet', 'güzel', 14000), ('yasin', 'taka', 18000),
##           ('metin', 'kobay', 21000), ('selim', 'ayancı', 25000)]
##
##komut_ekle = '''INSERT INTO calısanlar (ad, soyad, maas) VALUES (?, ?, ?)'''
##
##cur.executemany(komut_ekle, veriler)
##print('eklemeler başarılı!!')
#
#cur.execute('''SELECT * FROM sqlite_master WHERE type = 'table' ''')
#tables = cur.fetchall()
#
#for i in tables:
#    print(i)
#
#
#conn.commit()
#conn.close()

conn = sql.connect('ders.db')
cur = conn.cursor()

#cur.execute('''CREATE TABLE patronlar
#(id integer PRIMARY KEY, ad text, soyad text, maas integer)''')

#veriler = [('yiğit', 'aslan', 580000), ('metin', 'gülsever', 670000),
#           ('vedat', 'akın', 640000), ('ali', 'tekin', 690000)]
#komut_ekle = '''INSERT INTO patronlar (ad, soyad, maas) VALUES (?,?,?)'''
#
#cur.executemany(komut_ekle, veriler)


#cur.execute('''SELECT * FROM calısanlar WHERE ad like 'ib_____' ''')
#list_all = cur.fetchall()
#
#for i in list_all:
#    print(i)

cur.execute('''SELECT * FROM sqlite_master WHERE type = 'table' ''')
tables = cur.fetchall()

for i in tables:
    print(i)


conn.commit()
conn.close()





