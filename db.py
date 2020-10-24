# -*- coding: utf-8 -*-
'''
create table users(
    id int not null auto_increment, 
    name varchar(100) not null,
    pass varchar(100) not null,
    primary key(id)
);
'''
import mysql.connector      # pip install mysql-connector
import util
config = util.get_config()
USER = config["user"]
PASSWORD = config["password"]
DATABASE = config["database"] 

def get_connect():
    conn = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE)    
    return conn


def save_user(username, password):
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('insert into users(name, pass) values(%s, %s)', (username, password))
        conn.commit()
    except Exception as e:
        print(e)
        if conn:
            conn.rollback()
    finally:
        cursor.close()
        conn.close()

def get_pass(username):
    try:
        conn = get_connect()
        cursor = conn.cursor()
        # 这里使用(username)会报错
        cursor.execute('select pass from users where name = %s', (username,))
        password = cursor.fetchall()
    except Exception as e:
        print(e)        
    finally:
        cursor.close()
        conn.close()
    if not password:
        return password
    else:
        return password[0][0]

if __name__ == '__main__':
    save_user("xhh", "123")
    print(get_pass("xhh"))
