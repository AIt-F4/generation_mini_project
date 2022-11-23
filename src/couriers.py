"""
contains the courier class and all fuction related to them
"""

import pymysql
from simple_term_menu import TerminalMenu as menu
import pandas

def import_couriers():
    connection = pymysql.connect(host='localhost', 
                                 user='root',password='password', 
                                 database ='mini_project', 
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection as connect:
        with connect.cursor() as cursor:
            sql = "SELECT * FROM couriers"
            cursor.execute(sql)
            return cursor.fetchall()
def export_couriers():
    connection = pymysql.connect(host='localhost', 
                                      user='root',password='password', 
                                      database ='mini_project', 
                                      cursorclass=pymysql.cursors.DictCursor)


    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, phone FROM couriers"
            cursor.execute(sql)
            all_couriers_data = cursor.fetchall()
    #print(all_products_data)
    all_id = []
    all_name = []
    all_phone= []
    for item in all_couriers_data:
        all_id.append(item['id'])
        all_name.append(item['name'])
        all_phone.append(item['phone'])
    dic_to_export = {'id':all_id,'name':all_name, 'price':all_phone}
    dataframe = pandas.DataFrame(dic_to_export)
    dataframe_csv = dataframe.to_csv('data/couriers.csv')

class Courier:
    def __init__(self,name, phone, courier_id= None):
        self._name = name
        self._phone = phone
        self.id = courier_id
    
    def write_courier(self):
        connection_couriers = pymysql.connect(host='localhost', 
                                      user='root',password='password', 
                                      database ='mini_project', 
                                      cursorclass=pymysql.cursors.DictCursor)
        with connection_couriers:
            with connection_couriers.cursor() as cursor:
                sql = f"INSERT INTO couriers(name, phone) VALUES('{self._name}','{self._phone}')"
                cursor.execute(sql)
            connection_couriers.commit()
            with connection_couriers.cursor() as cursor:
                sql = f"SELECT id FROM couriers WHERE phone ='{self._phone}'"
                cursor.execute(sql)
                id_raw = cursor.fetchone()
                self.id = id_raw['id']
    
    
    def update_courier(self):
        """
        takes no parameters
        updates the courier in the table according to user inputs
        """
        options = ['name','phone','both']
        choice =menu(options,title = 'What to update').show()
        if choice == 2:
            self._name = input('What is the new name for the courier?')
            self._price = float(input('What is the new phone of the courier'))
        elif choice == 0:
            self._name = input('What is the new name for the courier?') 
        elif choice == 1:
            self._price = float(input('What is the new phone of the courier?'))
        connection = pymysql.connect(host='localhost', 
                                     user='root',password='password', 
                                     database ='mini_project', 
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                sql = f"UPDATE couriers SET name = '{self._name}', price = {self._phone} WHERE id = {self.id}"
                cursor.execute(sql)
            connection.commit()
            
            
    def delete_courier(self):
        """takes no paramaters
            deletes the table entry for the courier
            returns nothing
        """
        connection = pymysql.connect(host='localhost', 
                                     user = 'root',password = 'password', 
                                     database = 'mini_project',
                                     cursorclass=pymysql.cursors.DictCursor) 
        with connection:
            with connection.cursor() as cursor:
                sql =f"DELETE FROM couriers WHERE id = {self.id}"
                cursor.execute(sql)
            connection.commit()
            




x = import_couriers()
couriers_list = []
for item in x:
    couriers_list.append(Courier(item["name"],item["phone"],item["id"]))

courier_names = []
for item in couriers_list:
    courier_names.append(item._name)
    
export_couriers()
