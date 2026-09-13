# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator

**Name:** Jeanne Audrey R. Autentico
**Section:** 8 - Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Non-empty string | Presence Validation | "" | Cannot be black spaces | Student name is required. |
| Age | Integer number | Data type + range | fourteen, 10, 19 | Must be a valid integer and between 11 and 18 | Your age should be a number and you should be in the range of 11 - 18 |
| Grade Level | Integer value | Acceptable value | 13, 6, G8 | Must be 7, 8, 9, 10, 11, 12 | Invalid grade level |
| Email Address | Text string | Simple Pattern | studentpshs.edu.ph | Must contain both '@' and '.' characters | Invalid email address format. |
| Registration Code | Text string | Length Validation | ABC, ABCDEFG | Must be exactly 6 characters long | The registration code must contain exactly 6 characters. |
---
## Validation Questions
### 1. Why should the student name not be blank?
> Every student must have a name. If nothing was typed in it would mean that no one would be registering. 
### 2. Why should age be checked for both data type and range?
> We check the data type to make sure the person, who is registering, typed an actual whole number; meanwhile, we check the range to make sure the student is between 11 and 18 years old, which is the required age group for the workshop.
### 3. Why should grade level only accept specific values?
> The program only accepts specific values from 7 to 12 because those are the only actual highschool grades. 
### 4. What format requirements did you use for the email address?
> The email must have both an "@" symbol and a "." dot. If it does not have these two characters, it cannot be a real email address.
### 5. What length requirement did you use for the registration code?
> The registration code must be exactly 6 characters long.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Flowchart
> N/A
>
OR
## Pseudocode

```text
START
    SET is_valid = True
    SET error_message = ""

    OUTPUT "Enter student name: "
    READ name
    IF name is empty or only spaces THEN
        is_valid = False
        error_message = "Student name is required."
    ENDIF

    IF is_valid IS True THEN
        OUTPUT "Enter age: "
        READ age_input
        TRY
            CONVERT age_input TO integer STORE IN age
            IF age < 11 OR age > 18 THEN
                is_valid = False
                error_message = "Age must be from 11 to 18."
            ENDIF
        EXCEPT
            is_valid = False
            error_message = "Age must be a number."
        ENDTRY
    ENDIF

    IF is_valid IS True THEN
        OUTPUT "Enter grade level: "
        READ grade
        IF grade NOT IN ["7", "8", "9", "10", "11", "12"] THEN
            is_valid = False
            error_message = "Invalid grade level."
        ENDIF
    ENDIF

    IF is_valid IS True THEN
        OUTPUT "Enter email: "
        READ email
        IF "@" NOT IN email OR "." NOT IN email THEN
            is_valid = False
            error_message = "Invalid email address format."
        ENDIF
    ENDIF

    IF is_valid IS True THEN
        OUTPUT "Enter registration code: "
        READ reg_code
        IF length of reg_code IS NOT EQUAL TO 6 THEN
            is_valid = False
            error_message = "The registration code must contain exactly 6 characters."
        ENDIF
    ENDIF

    OUTPUT "------------------------------"
    IF is_valid IS True THEN
        OUTPUT "REGISTRATION ACCEPTED"
        OUTPUT "------------------------------"
        OUTPUT "Student: " + name
        OUTPUT "Age: " + age
        OUTPUT "Grade Level: " + grade
        OUTPUT "Email: " + email
        OUTPUT "Registration Code: " + reg_code
    ELSE
        OUTPUT "REGISTRATION NOT ACCEPTED"
        OUTPUT "Reason: " + error_message
    ENDIF
END
```

Your design should show:
- user input
- validation decisions
- error messages
- accepted registration
- rejected registration.
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
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
```

---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Presence validation was used on the student name part. The program removes trailing spaces using .strip() and checks if the string is empty to make sure a blank response is blocked.
### Data Type Validation
Explain where you used data type validation.
> Data type validation was used on the age part. The program uses a try-except block with "int" to process inputs containing alphabetical words preventing system confusion.
### Range Validation
Explain where you used range validation.
> Range validation was also used on the age part. An if conditional checks whether the numeric value is in between the allowed boundaries of 11 to 18.
### Acceptable Value Validation
Explain where you used acceptable value validation.
> Acceptable value validation was used on the grade level part. The program checks if the string input exists within an explicit list of allowed high school grades ("7", "8", "9", "10", "11", "12").
### Pattern Validation
Explain the simple pattern rule you used.
> Pattern Validation was used on the email address part. The program checks whether the format entered was correct by checking if both the "@" symbol and a "." character exists anywhere inside the input.
### Length Validation
Explain the length rule you used.
> Length Validation was used on the registration code part. The program calls the len() function to recognize the rule that the text string contains exactly 6 characters.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
>
Write **PASS** when the actual output matches the expected output.
>
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- `input_validation.md`
- `workshop_validator_flowchart.png` if a flowchart was used
---

[← Back to Main Portfolio](../README.md)
