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
    data = [e[i].get() for i in range(2)]
    cursor.execute(f"call insert_service({int(data[0])}, '{data[1]}')")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_service_screen():
    global e
    root_func = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id услуги').grid(row=1, column=0)
    l2 = Label(root_func, text='Название услуги').grid(row=2, column=0)

    e = [None for i in range(2)]
    for i in range(0, 2):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Добавить', command=insert_service_sql).grid(row=3, column=1)

    for i in range(0, 2):
        e[i].grid(row=i + 1, column=1)


def delete_service_sql():
    data = [e[i].get() for i in range(1)]
    cursor.execute(f"call delete_service({int(data[0])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def delete_service_screen():
    global e
    root_func = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='id услуги').grid(row=1, column=0)

    e = [None for i in range(1)]
    for i in range(0, 1):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Удалить', command=delete_service_sql).grid(row=2, column=1)

    for i in range(0, 1):
        e[i].grid(row=i + 1, column=1)


def contract_info_sql():
    contr_root = Tk()
    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8",)
    table = ttk.Treeview(contr_root, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id контракта", anchor=W)
    table.heading("#2", text="id клиента", anchor=W)
    table.heading("#3", text="id работника", anchor=W)
    table.heading("#4", text="id услуги", anchor=W)
    table.heading("#5", text="id продукта", anchor=W)
    table.heading("#6", text="Статус оплаты", anchor=W)
    table.heading("#7", text="Статус выполнения", anchor=W)
    table.heading("#8", text="Магазин", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)
    table.column("#3", stretch=NO, width=100)
    table.column("#4", stretch=NO, width=100)
    table.column("#5", stretch=NO, width=100)
    table.column("#6", stretch=NO, width=100)
    table.column("#7", stretch=NO, width=100)
    table.column("#8", stretch=NO, width=100)
    # ---------------------------create table------------------------

    data = [e[i].get() for i in range(1)]
    cursor.execute(f"SELECT * FROM contract_info({int(data[0])})")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


def contract_info_screen():
    global e
    root_func = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    # l0 = Label(root_func, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, text='Ваш id ').grid(row=1, column=0)

    e = [None for i in range(1)]
    for i in range(0, 1):
        e[i] = Entry(root_func)
    b0 = Button(root_func, text='Вывести контракты', command=contract_info_sql).grid(row=2, column=1)

    for i in range(0, 1):
        e[i].grid(row=i + 1, column=1)


def client_info_screen_sql():
    prod_root = Tk()
    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3")
    table = ttk.Treeview(prod_root, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id клиента", anchor=W)
    table.heading("#2", text="ФИО клиента", anchor=W)
    table.heading("#3", text="email", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)
    table.column("#3", stretch=NO, width=100)

    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM client_info")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


# Подключение к существующей базе данных
connection = psycopg2.connect(dbname='tr_bog',
                              user="postgres",
                              password="SQL.666.SQl,",
                              host="127.0.0.1",
                              port="5432")

cursor = connection.cursor()  # create cursor


# close all
