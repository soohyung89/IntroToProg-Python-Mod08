# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Soohyung Lee,03/09/2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
menu_option = None

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Soohyung Lee,03/08/2021,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price
    # -- Properties --
    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() is False:
            self.__product_name = value
        else:
            raise Exception("Error: Product name cannot be numbers")

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if Product.is_float(value):
            self.__product_price = value
        else:
            raise Exception("Error: Product price must be numbers")

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # -- Methods --
    def to_string(self):
        return self.product_name + "," + str(self.product_price)

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

    def __doc__(self):
        return 'This class holds product and price data'


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Soohyung Lee,03/09/21,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """This function reads data from a file
        :param file_name: (string) with name of file
        :return: list_of_objects
        """
        list_of_objects = []
        try:
            f = open(file_name, 'r')
            for line in f:
                product, price = line.split(",")
                list_of_objects.append(Product(product, price.strip()))
        except:
            f = open(file_name, 'w')
        f.close()
        return list_of_objects


    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_objects):
        """This function saves the list of objects to a file
        :param file_name: (string) with name of file
        :param list_of_objects: (list) of product objects
        :return: success
        """
        f = open(file_name, 'w')
        for obj in list_of_objects:
            f.write(obj.product_name + ',' + obj.product_price + '\n')
        f.close()
        return 'success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Process data to and from a file and a list of product objects:

    methods:
        print_menu()
        input_menu_choice()
        display_current_data(list_of_objects): -> a list of Product objects
        get_product_data()
    """
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Display Current Data
        2) Add Product to List
        3) Save Data to File & Exit Program      
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string containing the user's choice
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def display_current_data(list_of_objects):
        """ Prints Product objects in the list to the user
        :param list_of_objects: list containing Product objects
        """
        if list_of_objects == []:
            print('\nThe product list is currently empty!')
        else:
            print('\nCurrent Products and Prices in List:')
            for obj in list_of_objects:
                print(obj.product_name + ', ' + obj.product_price)
    # TODO: Add code to get product data from user
    @staticmethod
    def get_product_data():
        """ Get product and price information from user then create new Product object
        :param: None
        :return: product object"""
        try:
            item = input('Please enter a product: ').strip()
            price = input('Please enter a price: ').strip()
            product_obj = Product(item, price)
        except Exception as e:
            print(e)

        return product_obj

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

try:
    # Load data from file into a list of product objects
    list_of_objects = FileProcessor.read_data_from_file(strFileName)

    # Show user a menu of options
    # Get user's menu option choice
    while menu_option != '3':
        IO.print_menu()
        menu_option = IO.input_menu_choice()
        if menu_option == '1':  # Display current data
            IO.display_current_data(list_of_objects)
        elif menu_option == '2':  # Add product to list
            list_of_objects.append(IO.get_product_data())
        elif menu_option == '3':
            FileProcessor.write_data_to_file(strFileName, list_of_objects)
            break
        else:
            continue
except Exception as e:
    print(e)