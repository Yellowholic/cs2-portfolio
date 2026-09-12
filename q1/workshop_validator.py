# Collecct all the inputs 
name = input("Enter student name: ").strip()
age_input = input("Enter age: ").strip()
grade = input("Enter grade level: ").strip()
email = input("Enter email: ").strip()
reg_code = input("Enter registration code: ").strip()

# Check validation rules
all_errors = "" 

# Checking Student Name
if name == "":
    all_errors = all_errors + "- Student name is required.\n"

# Checking Age
if age_input.isdigit() == False:
    all_errors = all_errors + "- Your age should be a number and you should be in the range of 11 - 18\n"
else:
    if int(age_input) < 11 or int(age_input) > 18:
        all_errors = all_errors + "- Your age should be a number and you should be in the range of 11 - 18\n"

# Checking Grade Level
if grade not in ["7", "8", "9", "10", "11", "12"]:
    all_errors = all_errors + "- Invalid grade level.\n"

# Checking Email Address
if "@" not in email or "." not in email:
    all_errors = all_errors + "- Invalid email address format.\n"

# Checking Registration Code
if len(reg_code) != 6:
    all_errors = all_errors + "- The registration code must contain exactly 6 characters.\n"


# Print the results
print("------------------------------")

if all_errors != "":
    # If our error text is not empty, it means mistakes were found
    print("REGISTRATION NOT ACCEPTED")
    print("Reasons:")
    print(all_errors) 
else:
    # If our error text is still completely blank, everything is perfect
    print("REGISTRATION ACCEPTED")
    print("------------------------------")
    print("Student:", name)
    print("Age:", age_input)
    print("Grade Level:", grade)
    print("Email:", email)
    print("Registration Code:", reg_code)
