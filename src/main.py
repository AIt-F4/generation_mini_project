"""
Author: Luca Tierney
"""

from simple_term_menu import TerminalMenu as menu
from products import Product,products_names, products_list, export_products
from couriers import Courier,courier_names,couriers_list, export_couriers 
from file_handling import Files
import os
from orders import Order
import pymysql.cursors
import pandas

os.system("clear")

#creating an empty list of products, placeholder
products = products_list
#creating an empty list for orders for orders
orders = [{'customer_name':'Luca','cus_adress': '95 lawrence avenue','cus_phone':'07949809239', 'status':'preparing'},{'customer_name':'David','cus_adress':'amberton grove', 'cus_phone':'09321309', 'status':'done'}]

couriers = couriers_list
#creating the options for the main menu
options = ['[1] Products','[2] Orders', '[3] Couriers', '[4] Export', '[0] Quit']
#creating the otions for the producs sub menu
products_options = ['[1] View all products','[2] Create a product', '[3] Update a product', '[4] Delete a Product','[0] Quit']
order_options = ['[1] View all orders','[2] Create an order', '[3] Update an order', '[4] Delete an order','[0] Quit']
courier_options =['[1] View all couriers','[2] Create a courier', '[3] Update a courier', '[4] Delete a courier','[0] Quit']

statuses = ['preparing','prepared', 'delivering', 'delivered']
#creating the main menu
main_menu = menu(options, title ='Main Menu')
#creating the producsts menu
products_menu = menu(products_options, title = 'Products Options' )
#creating orders menu
orders_menu = menu(order_options, title = 'Order Options')
#creating courier menu5
courier_menu = menu(courier_options, title = 'Couriers')


def product_choices():
    """
    takes no arguements
    logic for the product menu and all options relating
    """
    products_running = True
    #starts the products while loop and creates a menu for the options 
    while products_running == True:
        products_choice = products_options[products_menu.show()]
        #takes the users choice and does what they chose
        if products_choice == '[0] Quit':
            products_running = False
        elif products_choice == '[2] Create a product':
            while True:
                new_name = input('What is the new products name?')
                try:
                    new_price = float(input('What is the price of the new product? (float)'))
                except:
                    continue
                
                products.append(Product(new_name,new_price))
                products_names.append(new_name)
                products[-1].write_products()
                print(f'Added product {new_name} at index {len(products)-1}')
                break
        elif products_choice == '[1] View all products':
            for item in products:
                print(item._name,item._price)
        elif products_choice == '[3] Update a product':
            print('Which product would you like to update?')
            os.system("clear")
            choice = menu(products_names, title = 'Products').show()
            products[choice].update_product()
        elif products_choice == '[4] Delete a Product':
            print('Which product would you like to delete?')
            choice = menu(products_names, title = 'Products').show()
            products[choice].delete_product()
            del products[choice]
            del products_names[choice]


def orders_choices():
    """
    takes no arguements
    order menu logic
    """
    orders_running = True
    while orders_running == True:
        # lets the user pick between  viewing creating and deleting orders
        order_choice = order_options[orders_menu.show()]
        if order_choice == '[0] Quit':
            orders_running = False
        elif order_choice =='[1] View all orders':
            print(orders)
        elif order_choice =='[2] Create an order':
            status = statuses[menu(statuses, title = 'Which status is the order?').show()]
            contents = []
            while True:
                
                contents_menu = products_names.copy()
                contents_menu.append('[0] Quit')
                contents_choice = contents_menu[menu(contents_menu, title = 'What is the contents of the order?').show()]
                if contents_choice == '[0] Quit':
                    break
                else:
                    contents.append(contents_choice)
                    print(contents)
            courier = couriers[menu(courier_names, title='Who is the courier for this order?').show()]
            new_order = Order(
                input('What is the customers name?'),
                input('What is the customers adress?'),
                input('What is the customers phone?'),
                status,
                contents,
                courier
                )
            orders.append(new_order.dic)
        elif order_choice =='[3] Update an order':
            order_option = []
            count = 0
            for item in orders:
                order_option.append('['+str(count)+'] '+item['cus_adress'])
                count +=1
            print('Which order would you like to modify?')
            choice = menu(order_option, title = 'Orders').show()
            # print('What would you like to update?')
            # x = list(orders[choice].items())
            # y = []
            # for item in x:
            #     y.append(item[0])
            # choice2 = menu(y).show()
            # if choice2 == 0:
            #     orders[choice].update({'customer_name':input('What is the customers name?')})
            #     print(orders[choice])
            # elif choice2 == 1:
            #     orders[choice].update({'cus_adress':input('What is the customers adress?')})
            #     print(orders[choice])
            # elif choice2 == 2:
            #     orders[choice].update({'cus_phone':input('What is the customers phone?')})
            #     print(orders[choice])
            
            #only allows orders to have certain statuses from a predetermined list
            #elif choice2 ==3:
            status_menu = menu(statuses, title = 'Which status is the order?').show()
            new_status = statuses[status_menu]
            orders[choice].update({'status':new_status})
        elif order_choice == '[4] Delete an order':
            order_option = []
            for item in orders:
                order_option.append(item['cus_adress'])
            choice2 = menu(order_option, title = 'Which order to delete').show()
            del orders[choice2]               


def couriers_choices():
    """
    takes no arguements
    logic for couriers menu
    """
    courier_running = True
    #starts the products while loop and creates a menu for the options 
    while courier_running == True:
        courier_choice = courier_options[courier_menu.show()]
        #takes the users choice and does what they chose
        if courier_choice == '[0] Quit':
            courier_running = False
        elif courier_choice == '[2] Create a courier':
            new_name = input('What is the name of the courier you want to add?')
            new_phone = input('What is the phone number of the courier?')
            couriers.append(Courier(new_name,new_phone))
            courier_names.append(new_name)
            couriers[-1].write_courier()
        elif courier_choice == '[1] View all couriers':
            for item in couriers:
                print(item._name,item._phone)
        elif courier_choice == '[3] Update a courier':
            print('Which courier would you like to update?')
            choice = menu(courier_names, title = 'Couriers').show()
            couriers[choice].update_courier()
            
        elif courier_choice == '[4] Delete a courier':
            print('Which courier would you like to delete?')
            choice = menu(couriers, title = 'Couriers').show()
            couriers[choice].delete_courier()
            del couriers[choice]
            del courier_names[choice]
            

def export_choices():
    """
    takes no arguements
    export logic
    """
    choice = menu(['Couriers','Products', 'Quit']).show()
    if choice == 0:
        print('Exporting couriers to couriers.csv')
        export_couriers()
    elif choice == 1:
        print('Exporting products to products.csv')
        export_products()
        

#if its running from this file starts while loop
if __name__ == "__main__":
    while True:
        #shows the menu and stores the users response
        options_choice =options[main_menu.show()]
        #if the users chooses to quit ends the while loop and ends the program
        if options_choice =='[0] Quit':
            break
        #if the user picks one shows the products menu
        elif options_choice =='[1] Products':
            product_choices()
        # if the user picks 2 shows the orders menu
        elif options_choice =='[2] Orders':
            orders_choices()
        elif options_choice =='[3] Couriers':
            couriers_choices()
        elif options_choice =='[4] Export':
            export_choices()
            