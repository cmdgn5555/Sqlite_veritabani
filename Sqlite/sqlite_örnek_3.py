
import sqlite3

conn = sqlite3.connect('soccer.db')
cur = conn.cursor()
conn.commit()

table = cur.execute('CREATE TABLE IF NOT EXISTS futbolcular(ad text, soyad text, takım text, maaş int)')
conn.commit()



def veri_ekle(ad, soyad, takım, maas):
    kayit = '''INSERT INTO futbolcular VALUES (?,?,?,?)'''
    cur.execute(kayit, (ad, soyad, takım, maas))
    conn.commit()

#veri_ekle('hakan', 'şükür', 'galatasaray', 35000)




def veri_ekle2():
    ad = input('ad: ')
    soyad = input('soyad: ')
    takım = input('takım: ')
    maaş = int(input('maaş: '))

    cur.execute('INSERT INTO futbolcular VALUES (?,?,?,?)', (ad, soyad, takım, maaş))
    conn.commit()

#veri_ekle2()



def veriler_getir():
    sorgu = '''SELECT * FROM futbolcular'''
    cur.execute(sorgu)
    listeye_ekle = cur.fetchall()
    for i in listeye_ekle:
        print(i)

#veriler_getir()




def istenen_kritere_göre_veri_getir(takımı):
    sorgu = '''SELECT * FROM futbolcular WHERE takım = ?'''
    cur.execute(sorgu, (takımı,))
    listeye_ekle = cur.fetchall()
    for i in listeye_ekle:
        print(i)

#istenen_kritere_göre_veri_getir('beşiktaş')




def kayit_guncelle(eskimaas, yenimaas, yeniad, yenisoyad, yenitakım):
    sorgu = '''UPDATE futbolcular SET ad = ?, soyad = ?, takım = ?, maaş = ? WHERE maaş = ?'''
    cur.execute(sorgu, (yeniad, yenisoyad, yenitakım, yenimaas, eskimaas))
    conn.commit()

#kayit_guncelle('35000', '60000', 'ogün', 'boncuk', 'bayrampaşaspor')




def kayit_sil(soyadı):
    sorgu = '''DELETE FROM futbolcular WHERE soyad = ?'''
    cur.execute(sorgu, (soyadı,))
    conn.commit()

#kayit_sil('boncuk')




def tablo_sil():
    conn = sqlite3.connect('soccer.db')
    cur = conn.cursor()
    cur.execute('''DROP TABLE futbolcular''')
    conn.commit()

tablo_sil()


conn.close()
