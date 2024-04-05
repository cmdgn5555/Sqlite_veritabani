
import sqlite3 as sql

conn = sql.connect('kayit.db')
cur = conn.cursor()
conn.commit()

table = cur.execute('CREATE TABLE IF NOT EXISTS barbaros(ad text, soyad text, sirket text)')
conn.commit()

def kayit_ekle(ad,soyad,sirket):
    try:
        ekle = 'INSERT INTO barbaros(ad, soyad, sirket) VALUES (?,?,?)'
        cur.execute(ekle,(ad,soyad,sirket))
        conn.commit()
        print('kayıt eklendi...')
    except:
        print('kayıt eklenemedi!!!')

#kayit_ekle('nurullah', 'taylan', 'jetpa holding')

def kayit_listele():
    sorgu = 'SELECT * FROM barbaros'
    cur.execute(sorgu)
    tüm_liste = cur.fetchall()
    for i in tüm_liste:
        print(i)

#kayit_listele()

def kayit_sil(sirketi):
    sorgu = 'DELETE FROM barbaros WHERE sirket = ?'
    try:
        cur.execute(sorgu,(sirketi,))
        conn.commit()
        print('kayıt silindi...')
    except:
        print('kayıt silinemedi!!!')

#kayit_sil('sanko holding')

def sirkete_göre_listele(sirketi):
    sorgu = 'SELECT * FROM barbaros WHERE sirket = ?'
    cur.execute(sorgu,(sirketi,))
    liste = cur.fetchall()
    for i in liste:
        print(i)

sirkete_göre_listele('albayrak holding')


