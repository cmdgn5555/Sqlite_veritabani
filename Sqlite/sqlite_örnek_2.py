import os.path
import sqlite3 as sql

class veritabani():

    def __init__(self):
        self.dizin = os.path.dirname(os.path.abspath('C:/Users/5530/PycharmProjects/pythonProject2'))
        self.vt_yol = os.path.join(self.dizin, 'okul.db')



    def baglanti_ac(self):
        try:
            self.conn = sql.connect(self.vt_yol)
            self.cur = self.conn.cursor()
        except:
            print('vt bağlantı hatası')



    def tablo_olustur(self):
        self.baglanti_ac()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students(numara integer PRIMARY KEY, adsoyad text, sinif text, durum text)''')
        self.conn.commit()
        self.baglanti_kapat()



    def tumsorgu(self):
        self.baglanti_ac()
        self.cur.execute('''SELECT * FROM students''')
        ogrencibilgiler = self.cur.fetchall()
        self.baglanti_kapat()
        return ogrencibilgiler



    def ogrencinumarasisorgu(self,numara):
        try:
            self.baglanti_ac()
            self.cur.execute('SELECT * FROM students WHERE numara = ?', (numara))
            ogrencibilgiler = self.cur.fetchall()
            self.baglanti_kapat()
            return ogrencibilgiler
        except:
            return []



    def ogrencidetaylisorgu(self, kolonlar, nereden, ne):
        try:
            self.baglanti_ac()
            komut = '''SELECT {} FROM students WHERE {} = '{}' '''.format(kolonlar, nereden, ne)
            self.cur.execute(komut)
            print(komut)
            ogrencibilgiler = self.cur.fetchall()
            self.baglanti_kapat()
            return ogrencibilgiler
        except:
            print(komut)
            return []



    def kayitekle(self, adsoyad, sinif, durum):
        try:
            self.baglanti_ac()
            self.cur.execute('INSERT INTO students (adsoyad, sinif, durum) VALUES (?, ?, ?)', (adsoyad, sinif, durum))
            self.conn.commit()
            self.baglanti_kapat()
            return 1
        except:
            return 0



    def kayitsil(self, numara):
        try:
            self.baglanti_ac()
            self.cur.execute('DELETE FROM students WHERE numara = ?', (numara))
            self.conn.commit()
            self.baglanti_kapat()
            return 1
        except:
            return 0



    def kayitguncelle(self, numara, adsoyad, sinif, durum):
        try:
            self.baglanti_ac()
            self.cur.execute('UPDATE students SET adsoyad = ?, sinif = ?, durum = ? WHERE numara = ?', (adsoyad, sinif, durum, numara))
            self.conn.commit()
            self.baglanti_kapat()
            return 1
        except:
            return 0



    def baglanti_kapat(self):
        self.conn.close()



vt_objesi = veritabani()