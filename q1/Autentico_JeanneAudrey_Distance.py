from math import sqrt, pow

x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"The distance of the 2 coordinates is {distance:.2f}")

# Reflection:
# The math library helped me simplify my program by instead of letting me type in a slightly complex program. It allowed me to simplify it and make it shorter by using sqrt and pow. 
# It helped me by making my program more simple and more shorter. Its more understandable, because i can find syntax error more easily.
# I would need to type in a longer program that would have cost me a lot of time looking for the syntax error. if the math library wasnt available it would be harder to find syntax errors especially if you are new to coding and dont know what to do. 
