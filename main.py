from tkinter import *
from function_seller import *
from function_manager import *
from function_director import *


# screen seller
def seller_screen():
    root_sale = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    lab_start1 = Label(root_sale, width=40, text="Что нужно сделать?")
    but_insert_product = Button(root_sale, width=40, text='Добавить товар', bg='#9ba0ab',
                                command=insert_product_screen)
    but_insert_contract_p = Button(root_sale, width=40, text='Добавление контрактов по продаже ', bg='#9ba0ab',
                                   command=insert_contract_p_screen)
    but_reserve_product = Button(root_sale, width=40, text='Резерв продукции ', bg='#9ba0ab',
                                 command=reserve_product_screen)
    lab_start2 = Label(root_sale, width=40, text="Что нужно посмотреть?")
    but_product_info = Button(root_sale, width=40, text='Список товаров ', bg='#9ba0ab',
                              command=product_info_screen_sql)
    but_service_info = Button(root_sale, width=40, text='Список услуг ', bg='#9ba0ab',
                              command=service_info_screen_sql)
    # -----------------------create widgets----------------------------------------------------------------

    # put widgets
    lab_start1.grid(row=0, column=0)
    but_insert_product.grid(row=1, column=0)
    but_insert_contract_p.grid(row=2, column=0)
    but_reserve_product.grid(row=3, column=0)
    lab_start2.grid(row=0, column=1)
    but_product_info.grid(row=1, column=1)
    but_service_info.grid(row=2, column=1)


# screen manager
def man_screen():
    root_man = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    lab_start1 = Label(root_man, width=40, text="Что нужно сделать?")
    but_insert_client = Button(root_man, width=40, text='Добавить клиента', bg='#9ba0ab',
                               command=insert_client_screen)
    but_insert_contract_u = Button(root_man, width=40, text='Добавленить контракт по услугам', bg='#9ba0ab',
                                   command=insert_contract_u_screen)
    but_status_contract = Button(root_man, width=40, text='Измененить статус контракта', bg='#9ba0ab',
                                 command=status_contract_screen)
    but_insert_service = Button(root_man, width=40, text='Добавить услугу', bg='#9ba0ab',
                                command=insert_service_screen)
    but_delete_service = Button(root_man, width=40, text='Удалить услугу', bg='#9ba0ab',
                                command=delete_service_screen)

    lab_start2 = Label(root_man, width=40, text="Что нужно посмотреть?")
    but_contract_info = Button(root_man, width=40, text='Список контрактов для своего магазина', bg='#9ba0ab',
                               command=contract_info_screen)
    but_client_info = Button(root_man, width=40, text='Список клиентов', bg='#9ba0ab',
                             command=client_info_screen_sql)
    but_service_info = Button(root_man, width=40, text='Список услуг ', bg='#9ba0ab',
                              command=service_info_screen_sql)  # from seller
    but_product_info = Button(root_man, width=40, text='Список продуктов ', bg='#9ba0ab',
                              command=product_info_screen_sql)  # from seller
    # -----------------------create widgets----------------------------------------------------------------

    # put widgets
    lab_start1.grid(row=0, column=0)
    but_insert_client.grid(row=1, column=0)
    but_insert_contract_u.grid(row=2, column=0)
    but_status_contract.grid(row=3, column=0)
    but_insert_service.grid(row=4, column=0)
    but_delete_service.grid(row=5, column=0)

    lab_start2.grid(row=0, column=1)
    but_contract_info.grid(row=1, column=1)
    but_client_info.grid(row=2, column=1)
    but_service_info.grid(row=3, column=1)
    but_product_info.grid(row=4, column=1)


# screen director
def dir_screen():
    root_dir = Tk()

    # -----------------------create widgets----------------------------------------------------------------
    lab_start1 = Label(root_dir, width=40, text="Что нужно сделать?")

    but_insert_employ = Button(root_dir, width=40, text='Добавить сотрудника ', bg='#9ba0ab',
                               command=insert_employ_screen)
    but_delete_employ = Button(root_dir, width=40, text='Уволить сотрудника ', bg='#9ba0ab',
                               command=delete_employ_screen)
    but_insert_client = Button(root_dir, width=40, text='Добавить клиента', bg='#9ba0ab',
                               command=insert_client_screen)  # from manager
    but_insert_product = Button(root_dir, width=40, text='Добавить товар', bg='#9ba0ab',
                                command=insert_product_screen)  # from seller
    but_insert_service = Button(root_dir, width=40, text='Добавить услугу', bg='#9ba0ab',
                                command=insert_service_screen)  # from manager
    but_delete_service = Button(root_dir, width=40, text='Удалить услугу', bg='#9ba0ab',
                                command=delete_service_screen)  # from manager
    but_update_contract = Button(root_dir, width=40, text='Изменить контракт ', bg='#9ba0ab',
                                 command=update_contract_screen)
    but_insert_contract_u = Button(root_dir, width=40, text='Добавленить контракт по услугам', bg='#9ba0ab',
                                   command=insert_contract_u_screen)  # from manager
    but_insert_contract_p = Button(root_dir, width=40, text='Добавление контрактов по продаже ', bg='#9ba0ab',
                                   command=insert_contract_p_screen)  # from seller

    lab_start2 = Label(root_dir, width=40, text="Что нужно посмотреть?")
    but_contract_all_info = Button(root_dir, width=40, text='Список всех контрактов', bg='#9ba0ab',
                                   command=contract_all_info_screen_sql)
    but_contract_join_info = Button(root_dir, width=40, text='Список всех контрактов с краткой расшифровкой', bg='#9ba0ab',
                                    command=contract_join_info_screen_sql)
    but_employs_info = Button(root_dir, width=40, text='Список сотрудников', bg='#9ba0ab',
                              command=employs_info_screen_sql)
    but_client_info = Button(root_dir, width=40, text='Список клиентов', bg='#9ba0ab',
                             command=client_info_screen_sql)  # from manager
    but_service_info = Button(root_dir, width=40, text='Список услуг ', bg='#9ba0ab',
                              command=service_info_screen_sql)  # from seller
    but_product_info = Button(root_dir, width=40, text='Список продуктов ', bg='#9ba0ab',
                              command=product_info_screen_sql)  # from seller
    # -----------------------create widgets----------------------------------------------------------------

    # put widgets
    lab_start1.grid(row=0, column=0)
    but_insert_employ.grid(row=1, column=0)
    but_delete_employ.grid(row=2, column=0)
    but_update_contract.grid(row=4, column=0)
    but_insert_client.grid(row=3, column=0)
    but_insert_contract_u.grid(row=5, column=0)
    but_insert_contract_p.grid(row=6, column=0)
    but_insert_product.grid(row=7, column=0)
    but_insert_service.grid(row=8, column=0)
    but_delete_service.grid(row=9, column=0)

    lab_start2.grid(row=0, column=1)
    but_contract_all_info.grid(row=1, column=1)
    but_contract_join_info.grid(row=2, column=1)
    but_employs_info.grid(row=3, column=1)
    but_client_info.grid(row=4, column=1)
    but_service_info.grid(row=5, column=1)
    but_product_info.grid(row=6, column=1)


root = Tk()  # create window

# create widgets
greetings = Label(width=40, text="Приветствую вас!\nВыберите вашу должность")
sale_button = Button(text="Продавец", command=seller_screen)
men_button = Button(text="Менеджер", command=man_screen)
dir_button = Button(text="Директор", command=dir_screen)

# put widgets
greetings.pack()
sale_button.pack()
men_button.pack()
dir_button.pack()

root.mainloop()
cursor.close()
connection.close()
