import psycopg2
from tkinter import *


def insert_employ_screen():
    pass


def delete_employ_screen():
    pass


def update_contract_screen():
    pass


def contract_all_info_screen():
    pass


def contract_join_info_screen():
    pass


def employs_info_screen():
    pass







# Подключение к существующей базе данных
connection = psycopg2.connect(dbname='tr_bog',
                              user="postgres",
                              password="SQL.666.SQl,",
                              host="127.0.0.1",
                              port="5432")

cursor = connection.cursor()  # create cursor


# close all
cursor.close()
connection.close()