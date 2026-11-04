def calculate_printing_cost(page, price_per_page):
  return page * price_per_page

def calculate_balance(payment, total_cost):
  return payment - total_cost

page = int(input("Enter the number of pages being printed: "))
payment = float(input("Enter amount paid: "))
price_per_page = 3.00

total_cost = calculate_printing_cost(page, price_per_page)
balance = calculate_balance(payment, total_cost)

print("Total Cost: PHP", total_cost)

if balance > 0:
  print("Your change is: PHP", balance)

if balance == 0:
  print("You paid the right amount! You may proceed.")

if balance < 0:
  short = abs(balance)
  print("Not enough money! Amount of cash still needed: PHP", short)
