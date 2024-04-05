
import sqlite3 as sql

# tablo oluşturma -> create table tablo_ismi (col1 text, col2 int, col3 text)


#con = sql.connect('student.db')
#
#cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS grade (name TEXT, lesson TEXT, grade INT)')
#con.commit()


#con = sql.connect('futbolcu.db')
#
#cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS takım (isim TEXT, yaş TEXT, maaş INT)')
#con.commit()

#con = sql.connect('personel.db')
#
#cur = con.cursor()
#cur.execute('create table if not exists şirket (isim text, soyisim text, bölüm text, yaş int, maaş int)')
#
#con.commit()
#
#

#con = sql.connect('ülke.db')
#
#cur = con.cursor()
#
#cur.execute('create table if not exists özellikler (nüfus int, parabirimi text, iklimi text, yerşekilleri text)')
#
#con.commit()

con = sql.connect('insan.db')

cur = con.cursor()

cur.execute('create table if not exists kişiselözellikler (boy int, kilo int, yaş int, ırk text, dil text, din text)')

con.commit()


con.close()