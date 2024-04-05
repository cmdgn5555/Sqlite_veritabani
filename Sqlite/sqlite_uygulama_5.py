
import sqlite3

veritabanı = 'test.db'

baglan = sqlite3.connect(veritabanı)

imlec = baglan.cursor()

def tablo_olustur():

    imlec.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    kitapadı TEXT NOT NULL, sayfasayısı INTEGER NOT NULL, yazaradı TEXT,
    kategori TEXT, raf TEXT NOT NULL)''')

    baglan.commit()

def tablo_kitap_ekle(kitap_adi:str, sayfa_sayisi:int, yazar_adi:str, kategori:str, raf:str):

    imlec.execute(f'INSERT INTO books (kitapadı, sayfasayısı, yazaradı, kategori, raf) VALUES (?,?,?,?,?)', (kitap_adi, sayfa_sayisi, yazar_adi, kategori, raf))

    baglan.commit()

#tablo_kitap_ekle('felekte gece', 712, 'mikhail pikolski', 'roman', '4e')


def tablo_bilgileri_oku():
    try:
        bilgiler = imlec.execute('''SELECT kitapadı, sayfasayısı, yazaradı, kategori, raf FROM books''')

        for i in bilgiler:
            print(i[4])
    except:
         print('böyle bi index yok!!!')

#tablo_bilgileri_oku()


def tablo_bilgileri_sil(id):

    imlec.execute(f'DELETE FROM books WHERE id = {id}')

    baglan.commit()

#tablo_bilgileri_sil(1)


def tablo_sil(tablo_adi):

    imlec.execute(f'DROP TABLE IF EXISTS {tablo_adi}')

    baglan.commit()

tablo_sil('books')


