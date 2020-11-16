import sqlite3
from models.user import User

class UserDbManager():
    TABLE_NAME = 'Users'

    @classmethod
    def get_user_by_email(cls, email):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        select_query = 'SELECT * FROM {} WHERE email=?'.format(cls.TABLE_NAME)
        result = cursor.execute(select_query, (email,))
        row = result.fetchone()

        if row:
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    
    @classmethod
    def get_user_by_id(cls, id):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()
        
        select_query = 'SELECT * FROM {} WHERE id=?'.format(cls.TABLE_NAME)
        result = cursor.execute(select_query, (id,))
        row = result.fetchone()

        if row:
            user = User(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def insert_user(cls, username, password, email):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        insert_query = 'INSERT INTO {table} VALUES(NULL, ?, ?, ?)'.format(table = cls.TABLE_NAME)

        cursor.execute(insert_query, (username, password, email))
        connection.commit()
        connection.close()
