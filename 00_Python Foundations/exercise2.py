#Exercise 2: Shopping Cart Program

item = input("What would you like to buy? ")
price = float(input("What is the price of the item? $"))
quantity = int(input("How many would you like to buy? "))
total_cost = price * quantity

print(f"You have added {quantity} {item}(s) to your cart. The total cost is: ${total_cost:.2f}")
