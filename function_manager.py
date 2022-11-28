import psycopg2
from tkinter import *
from tkinter import messagebox as mb
import tkinter.ttk as ttk


def insert_client_sql():
    data = [e[i].get() for i in range(3)]
    cursor.execute(f"call insert_client({int(data[0])}, '{(data[1])}',"
                   f"'{data[2]}')")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_client_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id клиента').grid(row=1, column=0)
    l2 = Label(root_func, text='ФИО клиента').grid(row=2, column=0)
    l3 = Label(root_func, text='email').grid(row=3, column=0)

    e = [None for i in range(3)]
    for i in range(0, 3):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=insert_client_sql).grid(row=4, column=1)

    for i in range(0, 3):
        e[i].grid(row=i + 1, column=1)


def insert_contract_u_sql():
    data = [e[i].get() for i in range(4)]
    cursor.execute(f"call insert_contract_u({int(data[0])}, {int(data[1])},"
                   f"{int(data[2])},{int(data[3])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_contract_u_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id контракта').grid(row=1, column=0)
    l2 = Label(root_func, text='id клиента').grid(row=2, column=0)
    l3 = Label(root_func, text='id сотрудника').grid(row=3, column=0)
    l4 = Label(root_func, text='id услуги').grid(row=4, column=0)

    e = [None for i in range(4)]
    for i in range(0, 4):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=insert_contract_u_sql).grid(row=9, column=1)

    for i in range(0, 4):
        e[i].grid(row=i + 1, column=1)


def status_contract_sql():
    data = [e[i].get() for i in range(3)]
    cursor.execute(f"call status_contract({int(data[0])}, {bool(int(data[1]))},"
                   f"{bool(int(data[2]))})")

    connection.commit()
    print(data[1], data[2])
    print(bool(int(data[1])), bool(int(data[2])))
    mb.showinfo(message='Успешно')


def status_contract_screen():
    global e
    root_func = Tk()
    root_func.attributes("-topmost", True)
    root_func.lift()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id контракта').grid(row=1, column=0)
    l2 = Label(root_func, text='Статус оплаты(1-опл, 0-нет)').grid(row=2, column=0)
    l3 = Label(root_func, text='Статус выполнения(1-опл, 0-нет)').grid(row=3, column=0)

    e = [None for i in range(3)]
    for i in range(0, 3):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=status_contract_sql).grid(row=4, column=1)

    for i in range(0, 3):
        e[i].grid(row=i + 1, column=1)


def insert_service_sql():
    pass


def insert_service_screen():
    pass


def delete_service_screen():
    pass


def contract_info_screen():
    pass


def client_info_screen():
    pass









# Подключение к существующей базе данных
connection = psycopg2.connect(dbname='tr_bog',
                              user="postgres",
                              password="SQL.666.SQl,",
                              host="127.0.0.1",
                              port="5432")

cursor = connection.cursor()  # create cursor


# close all
