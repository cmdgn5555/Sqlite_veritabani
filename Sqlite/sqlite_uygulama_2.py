
import sqlite3 as sql


def create_table():
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS kullanıcılar 
    (id integer PRIMARY KEY,
    name text, lastname text, 
    username text, password text, wage integer)''')

    conn.commit()
    conn.close()



def insert(name, lastname, username, password, wage):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    add_command = '''INSERT INTO kullanıcılar (name, lastname, username, password, wage) VALUES {} '''
    data = (name, lastname, username, password, wage)

    cur.execute(add_command.format(data))

    conn.commit()
    conn.close()



def print_all():
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    cur.execute(''' SELECT * FROM kullanıcılar ''')
    list_all = cur.fetchall()

    for i in list_all:
        print(i)

    conn.commit()
    conn.close()

    return list_all



def search_username_password(username, password):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE username = '{}' and password = '{}' '''
    cur.execute(search_command.format(username, password))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def search_username(username):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE username = '{}' '''
    cur.execute(search_command.format(username))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def search_password(password):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE password = '{}' '''
    cur.execute(search_command.format(password))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def search_name(name):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE name = '{}' '''
    cur.execute(search_command.format(name))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def search_lastname(lastname):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE lastname = '{}' '''
    cur.execute(search_command.format(lastname))

    user = cur.fetchone()


    conn.commit()
    conn.close()

    return user



def search_wage(wage):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    search_command = '''SELECT * FROM kullanıcılar WHERE wage = '{}' '''
    cur.execute(search_command.format(wage))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def update_wage(name, lastname, newwage):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    update_command = '''UPDATE kullanıcılar SET wage = '{}' WHERE name = '{}' and lastname = '{}' '''
    cur.execute(update_command.format(newwage, name, lastname))

    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user



def update_username_password(name, lastname, newusername, newpassword):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    update_command = '''UPDATE kullanıcılar SET username = '{}', password = '{}' WHERE name = '{}' and lastname = '{}' '''
    cur.execute(update_command.format(newusername, newpassword, name, lastname))

    conn.commit()
    conn.close()



def update_name_lastname(username, password, newname, newlastname):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    update_command = '''UPDATE kullanıcılar SET name = '{}', lastname = '{}' WHERE username = '{}' and password = '{}' '''
    cur.execute(update_command.format(newname, newlastname, username, password))

    conn.commit()
    conn.close()



def delete_account(username, password):
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    delete_command = '''DELETE FROM kullanıcılar WHERE username = '{}' and password = '{}' '''
    cur.execute(delete_command.format(username, password))

    conn.commit()
    conn.close()



def delete_table():
    conn = sql.connect('ders.db')
    cur = conn.cursor()

    cur.execute('''DROP TABLE kullanıcılar''')

    conn.commit()
    conn.close()


