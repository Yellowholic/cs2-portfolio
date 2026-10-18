def calculate_total(price, quantity):  
    return price * quantity  

def calculate_change(payment, total):
    return payment - total  

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total = calculate_total(price, quantity)

change = calculate_change(payment, total)

print("Total Cost: PHP", total)

if change >= 0:
    print("Change: PHP", change)
else:
    short = abs(change)
    print("Not enough money! Amount of cash still needed: PHP", short)

# Documentation Questions

# 1. What does each function do?
#    - calculate_total() multuplies the amount of items purchased and the price of the item being purchased
#    - calculate_change() subtracts total from payment to find the change/shortage.
#
# 2. What is the difference between parameters and actual arguments?
#    - Parameters are kinda like the "variables" inside the function definition.
#    - Arguments are the actual values passed when calling it.
#
# 3. Where is the returned total stored, and how is it reused?
#    - It is stored in the variable 'computed_total'. 
#    - It is reused by passing it as an argument into 'calculate_change()' and printing it.
#
# 4. Why is it useful to separate total calculation from change calculation?
#    - It makes code easier to understand, easier to fix, and lets you reuse one without the other getting in it's way
