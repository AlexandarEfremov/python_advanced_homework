from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Alex", 100.0)
        self.other = ShoppingCart("Ewcia", 200.0)

    def test_correct_init(self):
        self.assertEqual("Alex", self.cart.shop_name)
        self.assertEqual(100.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_lowercase(self):
        with self.assertRaises(Exception) as ex:
            self.cart.shop_name = "alex"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_remove_from_cart_should_raise_error(self):
        shop = ShoppingCart('Test', 200)
        with self.assertRaises(ValueError) as er:
            shop.remove_from_cart('product_name1')
        self.assertEqual('No product with name product_name1 in the cart!', str(er.exception))

    def test_remove_wrong_item_from_cart(self):
        with self.assertRaises(Exception) as ex:
            self.cart.remove_from_cart("cream")

        self.assertEqual("No product with name cream in the cart!", str(ex.exception))

    def test_shop_name_digits(self):
        with self.assertRaises(Exception) as ex:
            self.cart.shop_name = "Alex123"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_too_expensive(self):
        with self.assertRaises(Exception) as ex:
            self.cart.add_to_cart("cream", 101)

        self.assertEqual("Product cream cost too much!", str(ex.exception))

    def test_add_to_cart_successfully(self):
        ex_res = "cream product was successfully added to the cart!"
        self.assertEqual(ex_res, self.cart.add_to_cart("cream", 50))

    def test_add_to_cart_if_in_inventory(self):
        self.cart.add_to_cart("cream", 20)
        self.assertEqual({"cream": 20}, self.cart.products)

    def test_remove_available_item(self):
        self.cart.add_to_cart("cream", 20)

        ex_res = "Product cream was successfully removed from the cart!"
        self.assertEqual(ex_res, self.cart.remove_from_cart("cream"))

    def test_full_removal(self):
        self.cart.add_to_cart("cream", 20)
        self.cart.remove_from_cart("cream")
        self.assertEqual({}, self.cart.products)

    def test_empty_cart_again(self):
        self.cart.add_to_cart("cream", 20)
        self.cart.add_to_cart("books", 30)
        self.cart.add_to_cart("bread", 50)

        self.cart.remove_from_cart("cream")
        self.assertEqual({"books": 30, "bread": 50}, self.cart.products)

    def test_add_new_name(self):
        self.cart.add_to_cart("cream", 10)
        self.other.add_to_cart("books", 50)
        res = self.cart.__add__(self.other)

        self.assertEqual("AlexEwcia", res.shop_name)
        self.assertEqual(300, res.budget)
        self.assertEqual({"cream": 10, "books": 50}, res.products)

    def test_if_amount_is_larger_than_budget(self):
        self.cart.add_to_cart("cream", 50)
        self.cart.add_to_cart("milk", 60)
        with self.assertRaises(Exception) as ex:
            self.cart.buy_products()
        expected = f"Not enough money to buy the products! Over budget with {10:.2f}lv!"
        self.assertEqual(expected, str(ex.exception))

    def test_successful_purchase(self):
        self.cart.add_to_cart("cream", 50)
        ex = self.cart.buy_products()

        self.assertEqual('Products were successfully bought! Total cost: 50.00lv.', ex)

if __name__ == "__main__":
    main()