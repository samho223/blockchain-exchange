# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:05:29 2021

@author: sam
"""

import sqlite3
import pathlib

from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('successfully connect to db')
    except Error as e:
        print(f"The error '{e}' occur")
    return connection
        
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('cursor execute successfully')
    except Error as e:
        print(f"The error '{e}' occur")
        
current_path = str(pathlib.Path().absolute())
print(current_path)
database_path = current_path + '\\'
database_name = "test.sqlite"
connection = create_connection(database_path + database_name)



# create a table that stores user info
create_table_users = """
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL
  );
"""


cur = connection.cursor()
row= cur.execute("select * from users where name = 123")
connection.commit()
print(row.fetchall()[0][1])