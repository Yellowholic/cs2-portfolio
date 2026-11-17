def show_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

user_num = int(input("Enter a number: "))
show_table(user_num)

# For exercise 4, you need to create a function called show_table that uses a for loop from 1 to 10 to multiply and print the number.
# Outside the function, it asks the user to type a number and passes it into the function to show its multiplication table.
