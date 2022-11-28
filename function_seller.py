import psycopg2
from tkinter import *
from tkinter import messagebox as mb
import tkinter.ttk as ttk
# e = []


# ---------------seller start-------------------------------------
def insert_product_sql():
    data = [e[i].get() for i in range(8)]
    cursor.execute(f"call insert_product({int(data[0])}, '{(data[1])}',"
                 f"'{data[2]}','{data[3]}','{data[4]}',{int(data[5])},"
                 f"{int(data[6])},{int(data[7])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_product_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id товара').grid(row=1, column=0)
    l2 = Label(root_func, text='Имя товара').grid(row=2, column=0)
    l3 = Label(root_func, text='Магазин').grid(row=3, column=0)
    l4 = Label(root_func, text='Категория').grid(row=4, column=0)
    l5 = Label(root_func, text='Эра создания').grid(row=5, column=0)
    l6 = Label(root_func, text='Стоимость').grid(row=6, column=0)
    l7 = Label(root_func, text='Бронь').grid(row=7, column=0)
    l8 = Label(root_func, text='Количество').grid(row=8, column=0)
    e = [None for i in range(10)]
    for i in range(0, 8):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=insert_product_sql).grid(row=9, column=1)

    for i in range(0, 8):
        e[i].grid(row=i+1, column=1)


def insert_contract_p_sql():
    data = [e[i].get() for i in range(4)]
    cursor.execute(f"call insert_contract_p({int(data[0])}, {int(data[1])},"
                   f"{int(data[2])},{int(data[3])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_contract_p_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id контракта').grid(row=1, column=0)
    l2 = Label(root_func, text='id клиента').grid(row=2, column=0)
    l3 = Label(root_func, text='id сотрудника').grid(row=3, column=0)
    l4 = Label(root_func, text='id продукта').grid(row=4, column=0)

    e = [None for i in range(4)]
    for i in range(0, 4):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=insert_contract_p_sql).grid(row=9, column=1)

    for i in range(0, 4):
        e[i].grid(row=i + 1, column=1)


def reserve_product_sql():
    data = [e[i].get() for i in range(1)]
    cursor.execute(f"call reserve_product({int(data[0])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def reserve_product_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    ## -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id товара').grid(row=1, column=0)

    e = [None for i in range(1)]
    for i in range(0, 1):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Зарезервировать', command=reserve_product_sql).grid(row=9, column=1)

    for i in range(0, 1):
        e[i].grid(row=i + 1, column=1)


def product_info_screen_sql():
    prod_root = Tk()
    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8",)
    table = ttk.Treeview(prod_root, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id товара", anchor=W)
    table.heading("#2", text="Имя товара", anchor=W)
    table.heading("#3", text="Магазин", anchor=W)
    table.heading("#4", text="Категория", anchor=W)
    table.heading("#5", text="Эра создания", anchor=W)
    table.heading("#6", text="Стоимость", anchor=W)
    table.heading("#7", text="Бронь", anchor=W)
    table.heading("#8", text="Количество", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)
    table.column("#3", stretch=NO, width=100)
    table.column("#4", stretch=NO, width=100)
    table.column("#5", stretch=NO, width=100)
    table.column("#6", stretch=NO, width=100)
    table.column("#7", stretch=NO, width=100)
    table.column("#8", stretch=NO, width=100)
    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM product_info")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


def service_info_screen_sql():
    prod_root = Tk()
    # ---------------------------create table------------------------
    columns = ("#1", "#2")
    table = ttk.Treeview(prod_root, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id услуги", anchor=W)
    table.heading("#2", text="Название услуги", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)

    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM service_info")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


# ---------------seller end-------------------------------------


# Подключение к существующей базе данных
connection = psycopg2.connect(dbname='tr_bog',
                              user="postgres",
                              password="SQL.666.SQl,",
                              host="127.0.0.1",
                              port="5432")

cursor = connection.cursor()  # create cursor


# close all
