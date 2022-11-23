"""
contains product class and related functions
classes: Products
functions: import_products, export_products
"""

from simple_term_menu import TerminalMenu as menu
import pymysql
import pandas

def import_products():
    """
    takes no arguements
    returns a list of dictionarys containing all product information
    """
    connection = pymysql.connect(host='localhost', 
                                 user='root',password='password', 
                                 database ='mini_project', 
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection as connect:
        with connect.cursor() as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            return cursor.fetchall()

def export_products():
    """
    takes no arguements
    exports all the data in the product table to a csv
    """
    connection = pymysql.connect(host='localhost', 
                                      user='root',password='password', 
                                      database ='mini_project', 
                                      cursorclass=pymysql.cursors.DictCursor)


    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, price FROM products"
            cursor.execute(sql)
            all_products_data = cursor.fetchall()
    #print(all_products_data)
    all_id = []
    all_name = []
    all_price = []
    for item in all_products_data:
        all_id.append(item['id'])
        all_name.append(item['name'])
        all_price.append(item['price'])
    dic_to_export = {'id':all_id,'name':all_name, 'price':all_price}
    dataframe = pandas.DataFrame(dic_to_export)
    dataframe_csv = dataframe.to_csv('data/products.csv')    


#the class for all products
class Product:
    """
    attributes:
        name - string - name of the product
        price - float - price of the product
        id - int - products id in the sql table
    """
    def __init__(self, name, price_,product_id=None):
        self._name = name
        self._price = price_
        self.id = product_id
        
        
    #writes products to the database if they arent already in the database
    def write_products(self):
        connection = pymysql.connect(host='localhost', 
                                      user='root',password='password', 
                                      database ='mini_project', 
                                      cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                sql = f"INSERT INTO products(name, price) VALUES('{self._name}',{self._price})"
                cursor.execute(sql)
            connection.commit()
            with connection.cursor() as cursor:
                sql = f"SELECT id FROM products WHERE name ='{self._name}'"
                cursor.execute(sql)
                id_raw = cursor.fetchone()
                self.id = id_raw['id']
    
    #updates a product already in the database
    def update_product(self):
        """
        takes self as its only arguement
        updates the product in the table according to user inputs
        """
        options = ['name','price','both']
        choice =menu(options,title = 'What to update').show()
        if choice == 2:
            self._name = input('What is the new name for the product?')
            self._price = float(input('What is the new price of the product'))
        elif choice == 0:
            self._name = input('What is the new name for the product?') 
        elif choice == 1:
            self._price = float(input('What is the new price of the product?'))
        connection = pymysql.connect(host='localhost', 
                                     user='root',password='password', 
                                     database ='mini_project', 
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                sql = f"UPDATE products SET name = '{self._name}', price = {self._price} WHERE id = {self.id}"
                cursor.execute(sql)
            connection.commit()
            
            
    def delete_product(self):
        """
        takes self as its only arguement
        deletes the table entry for the product
        returns nothing
        """
        connection = pymysql.connect(host='localhost', 
                                     user = 'root',password = 'password', 
                                     database = 'mini_project',
                                     cursorclass=pymysql.cursors.DictCursor) 
        with connection:
            with connection.cursor() as cursor:
                sql =f"DELETE FROM products WHERE id = {self.id}"
                cursor.execute(sql)
            connection.commit()
                                     
                     
         
        
    #uses property decorator to make name a property so it has a getter and setter function
    @property
    def name(self):
        """
        takes self as its only arguement
        returns the products name attribute
        """
        print('Getting Name')
        return self._name

    #creates setter for the name property
    @name.setter
    def name(self,new_name):
        """
        takes self and new_name-string as arguemnts
        sets the _name attribute to be new_name
        """
        print('setting new name')
        if type(new_name) is str:
            self._name = new_name

    @property
    def price(self):
        """
        takes self as its only arguement
        returns the price attribute formated in dollars
        """
        
        return '${:,.2f}'.format(self._price)
    
    @price.setter
    def price(self, value):
        """
        takes self and int or float as arguements
        setter for the _price attribute
        """
        print('setting price')
        if type(value) is not float and type(value) is not int:
            print('not a valid price')
        self._price = float(value)
        



    

x = import_products()
products_list = []
for item in x:
    products_list.append(Product(item["name"],item["price"],item["id"]))

products_names = []
for item in products_list:
    products_names.append(item._name)
