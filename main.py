class Cake:
    def __init__(self, cake, price):
        self.cake = cake
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
class CakeOrder:
    def __init__(self):
        self.cakes = [
            Cake("Vanilla Cake", 20.00),
            Cake("Banana Cake", 30.00),
            Cake("Chocolate Cake", 25.00),
            Cake("Strawberry Cake", 40.00)
        ]

        self.order = []

        self.discount_code = "IBK_DISCOUNT"

        self.discount_percentage = 10

    def display_menu(self):
        print("/nCake Ordering Menu: ")

        for idx, cake in enumerate(self.cakes, 1):
            print(f"{idx}.{cake}")

    def add_to_order(self, cake_choice, quantity, message, total_price):
        cake = self.cakes[cake_choice - 1]

        total_price = cake.price * quantity

        self.order.append(cake_choice, quantity, total_price, message)

    def show_order(self):
        if not self.order:
            print("no item(s) ordered")
        else:
            print("/nYour order: ")

            total_amount = 0

            for item in self.order:
                print(f"{item[1]} x {item[0]} - ${item[2]:.2sf} (Message: {item[3]})")

                total_amount += item[2]

            print(f"\nTotal Amount: ${total_amount:.2sf}")

            self.apply_discount(total_amount)

    def apply_discount(self, total_amount):
        
        discount = 0 

        code = input("input your discount code (or press enter to skip) ").strip()

        if code == self.discount_code:
            dicount = total_amount - (self.discount_percentage/100)

            print(f"Discount applied: {self.discount_percentage}%")

        else:
            print("invalid discount code")

        final_amount = total_amount - discount

        print(f"Your final price is: {final_amount}:.2sf")

    def clear_order(self):
        self.order = []

    def main():
        cake_order = CakeOrder()

        while True:
            cake_order.display_menu()

            choice = input("input a number (1-4) to select desired cake of your choice, 0 to quit proogram")

            if choice.isdigit():
                choice = int(choice)

                if choice == 0:
                    cake_order.show_order()

                    break
                elif 1 <= choice <= 4:
                    quantity = input(f"input the quantity of for{cake_order.cakes[choice-1].name}: ")

                    if quantity.isdigit():
                        quantity = int(quantity)

                        message = input(f"input custom message for {cake_order.cakes[choice-1].name} (optional): ")

                        cake_order.add_to_order(choice, quantity, message)

                        print(f"Added {quantity} {cake_order.cakes[choice - 1].name}(s) to your order.")

                    else:
                        print("Invalid quantity. Please enter a number")

                else:
                    print("Invalid choice please enter a valid cake option")

            else:
                print("Invalid input. Please try again")

            continue_order = input("\nDo you want to order another cake? (y/n): ").lower()

            if continue_order != "y":
                cake_order.show_order()

                break

    if __name__ == "__main__":
        main()


