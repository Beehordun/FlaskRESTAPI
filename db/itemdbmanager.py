import sqlite3
from models.item import Item

class ItemDbManager():
    TABLE_NAME = "Items"

    @classmethod
    def insert_item(cls, name, price):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        insert_query = 'INSERT INTO {table} VALUES(?, ?)'.format(table = cls.TABLE_NAME)
        cursor.execute(insert_query, (name, price))
        connection.commit()
        connection.close()

    @classmethod
    def get_item_by_name(cls, name):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        get_by_name_query = 'SELECT * FROM {table} WHERE name=?'.format(table=cls.TABLE_NAME)

        result = cursor.execute(get_by_name_query, (name,))
        row = result.fetchone()

        if row:
             return Item(row[0], row[1])
        return None

    @classmethod
    def get_all_items(cls):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        get_all_query = 'SELECT * FROM {table}'.format(table=cls.TABLE_NAME)

        result = cursor.execute(get_all_query)
        rows = result.fetchall()
        
        items = []
        if len(rows) > 0:
            for row in rows:
                items.append(Item(row[0], row[1]))
        
        connection.close() 
        return items

    @classmethod
    def delete_items(cls, name):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        delete_query = 'DELETE FROM {table} WHERE name=?'.format(table=cls.TABLE_NAME)

        cursor.execute(delete_query, (name,))

        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item):
        connection = sqlite3.connect('flaskapi.db')
        cursor = connection.cursor()

        update_query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(update_query, (item.price, item.name))

        connection.commit()
        connection.close()
     