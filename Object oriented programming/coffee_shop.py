class CoffeeShop:
    def __init__(self):
        self.menu = {
            "Coffee": 150,
            "Tea": 100,
            "Cappuccino": 200
        }

    def show_menu(self):
        print("----- MENU -----")
        for item, price in self.menu.items():
            print(item, "-", price)

    def order(self, item):
        if item in self.menu:
            print(item, "ordered successfully.")
            print("Price:", self.menu[item])
        else:
            print("Item not available.")


shop = CoffeeShop()
shop.show_menu()
item = input("Enter your order: ")
shop.order(item)