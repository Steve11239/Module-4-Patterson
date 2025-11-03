
#Student: Steve Patterson
#Contact Phone: 248.783.6493
#Contact E-mail: hybridcalibratorsrule@gmail.com
#Contact E-mail: steven.patterson@csuglobal.edu
#Course Section: 25FD-CSC500-1 – Principles of Programming
#Course Module: Module 4: Portfolio Milestone

class ItemToPurchase: #define the class with required attributes (name, price, and quantity)
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity #calculate item cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

print("Item 1") #ask the user for item name, price, and quantity
name1 = input("Enter the item name: ")
price1 = float(input("Enter the item price: "))
quantity1 = int(input("Enter the item quantity: "))
item1 = ItemToPurchase(name1, price1, quantity1) #call the class with the item name, price, and quantity

print("\nItem 2") #ask the user for item name, price, and quantity
name2 = input("Enter the item name: ")
price2 = float(input("Enter the item price: "))
quantity2 = int(input("Enter the item quantity: "))
item2 = ItemToPurchase(name2, price2, quantity2) #call the class with the item name, price, and quantity

print("\nTOTAL COST")  #Calculate total cost of item one and two and display results
item1.print_item_cost()
item2.print_item_cost()

total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity) #total both items
print(f"\nTotal: ${total:.2f}")

