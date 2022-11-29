import psycopg2
from tkinter import *
from tkinter import messagebox as mb
import tkinter.ttk as ttk


def insert_employ_sql():
    data = [e[i].get() for i in range(5)]
    cursor.execute(f"call insert_employ({int(data[0])}, '{(data[1])}',"
                   f"'{data[2]}','{data[3]}','{data[4]}')")

    connection.commit()
    mb.showinfo(message='Успешно')


def insert_employ_screen():
    global e
    root_func = Tk()
    root_func.title('Добавление сотрудника')

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, width=20, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, width=20, text='id сотрудника').grid(row=1, column=0)
    l2 = Label(root_func, width=20, text='ФИО сотрудника').grid(row=2, column=0)
    l3 = Label(root_func, width=20, text='Документ').grid(row=3, column=0)
    l4 = Label(root_func, width=20, text='Должность').grid(row=4, column=0)
    l5 = Label(root_func, width=20, text='Магазин').grid(row=5, column=0)

    e = [None for i in range(5)]
    for i in range(0, 5):
        e[i] = Entry(root_func, width=40)
    b0 = Button(root_func, width=40, text='Добавить', command=insert_employ_sql).grid(row=6, column=1)

    for i in range(0, 5):
        e[i].grid(row=i + 1, column=1)


def delete_employ_sql():
    data = [e[i].get() for i in range(1)]
    cursor.execute(f"call delete_employ({int(data[0])})")

    connection.commit()
    mb.showinfo(message='Успешно')


def delete_employ_screen():
    global e
    root_func = Tk()
    root_func.title('Увольнение сотрудника')

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, width=20, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, width=20, text='id сотрудника').grid(row=1, column=0)

    e = [None for i in range(1)]
    for i in range(0, 1):
        e[i] = Entry(root_func, width=40)
    b0 = Button(root_func, width=40, text='Уволить', command=delete_employ_sql).grid(row=2, column=1)

    for i in range(0, 1):
        e[i].grid(row=i + 1, column=1)


def update_contract_sql():
    data = [e[i].get() for i in range(8)]
    if data[4] != '':
        cursor.execute(f"call update_contract({int(data[0])}, {int(data[1])},"
                       f"{int(data[2])},{int(data[3])},{int(data[4])},{bool(int(data[5]))},"
                       f"{bool(int(data[6]))},'{data[7]}')")
    else:
        cursor.execute(f"call update_contract({int(data[0])}, {int(data[1])},"
                       f"{int(data[2])},{int(data[3])},NULL,{bool(int(data[5]))},"
                       f"{bool(int(data[6]))},'{data[7]}')")

    connection.commit()
    mb.showinfo(message='Успешно')


def update_contract_screen():
    global e
    root_func = Tk()
    root_func.title('Изменение контракта')

    # -----------------------create widgets----------------------------------------------------------------
    l0 = Label(root_func, width=30, text='Заполните данные').grid(row=0, column=0)
    l1 = Label(root_func, width=30, text='id контракта').grid(row=1, column=0)
    l2 = Label(root_func, width=20, text='id клиента').grid(row=2, column=0)
    l3 = Label(root_func, width=30, text='id сотрудника').grid(row=3, column=0)
    l4 = Label(root_func, width=30, text='id услуги').grid(row=4, column=0)
    l5 = Label(root_func, width=30, text='id продукта').grid(row=5, column=0)
    l6 = Label(root_func, width=30, text='Статус оплаты(1-опл, 0-нет)').grid(row=6, column=0)
    l7 = Label(root_func, width=30, text='Статус выполнения(1-вып, 0-нет)').grid(row=7, column=0)
    l8 = Label(root_func, width=30, text='Магазин').grid(row=8, column=0)
    e = [None for i in range(8)]
    for i in range(0, 8):
        e[i] = Entry(root_func, width=40)
    b0 = Button(root_func, width=40, text='Изменить', command=update_contract_sql).grid(row=9, column=1)

    for i in range(0, 8):
        e[i].grid(row=i + 1, column=1)


def contract_all_info_screen_sql():
    root_func = Tk()
    root_func.title('Список контрактов')

    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8",)
    table = ttk.Treeview(root_func, columns=columns, show='headings')
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
    table.column("#7", stretch=NO, width=140)
    table.column("#8", stretch=NO, width=100)
    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM contract_all_info")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


def contract_join_info_screen_sql():
    root_func = Tk()
    root_func.title('Список контрактов')

    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")
    table = ttk.Treeview(root_func, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id контракта", anchor=W)
    table.heading("#2", text="ФИО клиента", anchor=W)
    table.heading("#3", text="ФИО работника", anchor=W)
    table.heading("#4", text="Название услуги", anchor=W)
    table.heading("#5", text="Название продукта", anchor=W)
    table.heading("#6", text="Статус выполнения", anchor=W)
    table.heading("#7", text="Магазин", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)
    table.column("#3", stretch=NO, width=100)
    table.column("#4", stretch=NO, width=100)
    table.column("#5", stretch=NO, width=120)
    table.column("#6", stretch=NO, width=100)
    table.column("#7", stretch=NO, width=100)

    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM contract_join_info")
    for i in cursor:
        table.insert("", END, values=tuple(i))
    connection.commit()


def employs_info_screen_sql():
    root_func = Tk()
    root_func.title('Список сотрудников')

    # ---------------------------create table------------------------
    columns = ("#1", "#2", "#3", "#4", "#5")
    table = ttk.Treeview(root_func, columns=columns, show='headings')
    table.pack(fill=BOTH, expand=1)

    table.heading("#1", text="id работника", anchor=W)
    table.heading("#2", text="ФИО работника", anchor=W)
    table.heading("#3", text="Документ", anchor=W)
    table.heading("#4", text="Должность", anchor=W)
    table.heading("#5", text="Магазин", anchor=W)
    table.column("#1", stretch=NO, width=100)
    table.column("#2", stretch=NO, width=100)
    table.column("#3", stretch=NO, width=100)
    table.column("#4", stretch=NO, width=100)
    table.column("#5", stretch=NO, width=100)

    # ---------------------------create table------------------------

    cursor.execute(f"SELECT * FROM employs_info")
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