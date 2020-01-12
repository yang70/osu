# Author: Matthew Yang
# Date: 01/10/2020
# Description:

#############
## CLASSES ##
#############

#
# Product Class
#
class Product:
    """
    """

    def __init__(self, id_code, title, description, price, quantity_available):
        """
        """
        self._id_code            = id_code
        self._title              = title
        self._description        = description
        self._price              = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        """
        """
        return self._id_code

    def get_title(self):
        """
        """
        return self._title

    def get_description(self):
        """
        """
        return self._description

    def get_price(self):
        """
        """
        return self._price

    def get_quantity_available(self):
        """
        """
        return self._quantity_available

    def decrease_quantity(self):
        """
        """
        if self._quantity_available > 0:
            self._quantity_available -= 1

        return self._quantity_available

#
# Customer Class
#
class Customer:
    """
    """

    def __init__(self, name, account_ID, is_premium_member):
        """
        """
        self._name              = name
        self._account_ID        = account_ID
        self._is_premium_member = is_premium_member
        self._cart              = []

    def get_name(self):
        """
        """
        return self._name

    def get_account_ID(self):
        """
        """
        return self._account_ID

    def is_premium_member(self):
        """
        """
        return self._is_premium_member

    def get_cart(self):
        """
        """
        return self._cart

    def add_product_to_cart(self, product_ID):
        """
        """
        self._cart.append(product_ID)

    def empty_cart(self):
        """
        """
        self._cart = []

    
    

#
# Store Class
#
class Store:
    """
    """

#######################
## ERROR DEFINITIONS ##
#######################

#
# Invalid Checkout Error
#
class OutOfRangeError(Exception):
    """
    """
    pass

############
## SCRIPT ##
############

def main():
    """
    """

if __name__ == '__main__':
    main()