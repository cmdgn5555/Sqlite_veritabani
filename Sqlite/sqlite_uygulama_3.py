
import sqlite3 as sql
vt = sql.connect('kitaplık_db.sqlite')
imlec = vt.cursor()

def ekle(kitap_id = '',kitap_adi = '', kitap_yazari = '', okunma_durumu = '', begeni = ''):
    imlec.execute('''CREATE TABLE IF NOT EXISTS kitaplık_tb(kitap_id INTEGER 
    PRIMARY KEY AUTOINCREMENT, kitap_adi, kitap_yazari, okunma_durumu, begeni)''')
    print(kitap_id, kitap_adi, kitap_yazari, okunma_durumu, begeni)

    kitap_girisi = '''INSERT INTO kitaplık_tb VALUES (?,?,?,?,?)'''

    imlec.execute(kitap_girisi, (kitap_id, kitap_adi, kitap_yazari, okunma_durumu, begeni))
    vt.commit()

def listele():
    imlec.execute('SELECT * FROM kitaplık_tb')
    kitaplar = imlec.fetchall()
    for i in kitaplar:
        for k in i:
            print(k, end=' ')
        print('')

def guncelle(guncellenecek):
    guncelle_kitap = input('güncel kitap adını giriniz: ')
    guncelle_yazar = input('güncel kitap yazarını giriniz: ')
    guncelle_okunma = input('güncel kitap okunma durumunu giriniz: ')
    guncelle_begeni = input('güncel kitap beğeni değerini giriniz: ')

    güncelleme_kodu = 'UPDATE kitaplık_tb SET kitap_adi = ?, kitap_yazari = ?, okunma_durumu = ?, begeni = ? WHERE kitap_id = ?'
    imlec.execute(güncelleme_kodu, (guncelle_kitap, guncelle_yazar, guncelle_okunma, guncelle_begeni, guncellenecek))
    vt.commit()

def sil(silinecek):
    silme_kodu = 'DELETE FROM kitaplık_tb WHERE kitap_id = ?'
    imlec.execute(silme_kodu, (silinecek))
    vt.commit()

def cikis():
    vt.close()
    print('çıkış yapıldı iyi günler...')