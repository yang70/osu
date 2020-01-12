# Author: Matthew Yang
# Date: 01/10/2020
# Description:

import unittest

from Store import Product, Customer

#############
# TEST DATA #
#############

TEST_DATA = {
    "products": [
        {
        "id_code": 1,
        "title": "apple",
        "description": "delicious red fruit",
        "price": 10,
        "quantity_available": 5
        },
        {
        "id_code": 2,
        "title": "orange",
        "description": "delicious orange fruit",
        "price": 15,
        "quantity_available": 3
        },
        {
        "id_code": 3,
        "title": "carrot",
        "description": "orange crunchy vegetable",
        "price": 5,
        "quantity_available": 7
        }
    ],
    "customers": [
        {
            "name": "Joe Schmoe",
            "account_ID": 123,
            "is_premium_member": True
        }
    ]
}

################
# TEST CLASSES #
################

#
# Tests for Product Class
#
class ProductTest(unittest.TestCase):
    """
    """
    def setUp(self):
        self.product_data = TEST_DATA["products"][0]
        self.product = Product(
            self.product_data["id_code"], 
            self.product_data["title"], 
            self.product_data["description"], 
            self.product_data["price"], 
            self.product_data["quantity_available"] 
        )

    def test_get_id_code(self):
        self.assertEqual(
            self.product.get_id_code(), 
            self.product_data["id_code"]
        )

    def test_get_title(self):
        self.assertEqual(
            self.product.get_title(), 
            self.product_data["title"]
        )

    def test_get_description(self):
        self.assertEqual(
            self.product.get_description(), 
            self.product_data["description"]
        )

    def test_get_price(self):
        self.assertEqual(
            self.product.get_price(), 
            self.product_data["price"]
        )

    def test_get_quantity_available(self):
        self.assertEqual(
            self.product.get_quantity_available(), 
            self.product_data["quantity_available"]
        )

    def test_decrease_quantity(self):
        self.assertEqual(
            self.product.decrease_quantity(), 
            self.product_data["quantity_available"] - 1
        )

    def test_decrease_quantity_if_zero(self):
        self.product._quantity_available = 0

        self.assertEqual(
            self.product.decrease_quantity(), 
            0
        )

#
# Tests for Customer Class
#
class CustomerTest(unittest.TestCase):
    """
    """
    def setUp(self):
        self.products      = []
        self.products_data = TEST_DATA["products"]

        for product_data in self.products_data:
            self.products.append(
                Product(
                    product_data["id_code"], 
                    product_data["title"], 
                    product_data["description"], 
                    product_data["price"], 
                    product_data["quantity_available"] 
                )
            )

        self.customer_data = TEST_DATA["customers"][0]

        self.customer = Customer(
            self.customer_data["name"],
            self.customer_data["account_ID"],
            self.customer_data["is_premium_member"]
        )

    def test_get_name(self):
        self.assertEqual(
            self.customer.get_name(),
            self.customer_data["name"]
        )

    def test_get_account_ID(self):
        self.assertEqual(
            self.customer.get_account_ID(),
            self.customer_data["account_ID"]
        )

    def test_is_premium_member(self):
        self.assertEqual(
            self.customer.is_premium_member(),
            self.customer_data["is_premium_member"]
        )

    def test_add_product_to_cart(self):
        self.assertListEqual(
            self.customer.get_cart(),
            []
        )

        for product in self.products:
            self.customer.add_product_to_cart(product.get_id_code())

        self.assertGreater(
            len(self.customer.get_cart()),
            0
        )

        self.assertListEqual(
            self.customer.get_cart(),
            [product.get_id_code() for product in self.products]
        )

    def test_empty_cart(self):
        for product in self.products:
            self.customer.add_product_to_cart(product.get_id_code())

        self.assertGreater(
            len(self.customer.get_cart()),
            0
        )

        self.customer.empty_cart()

        self.assertListEqual(
            self.customer.get_cart(),
            []
        )

#
# Tests for Store Class
#
class CustomerTest(unittest.TestCase):
    """
    """
            
if __name__ == '__main__':
    unittest.main()