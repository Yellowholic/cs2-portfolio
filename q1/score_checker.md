# Clean Decision Code Makeover: Student Score Checker
**Name:** Jeanne Audrey R. Autentico
>
**Section:** 8 - Dahlia
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.
---
# Part 1 - Analyze the Logic
## Input
What information does the program need?
> The program needs a revised version of the given code.

## Valid Range
**Minimum valid score:**
> 0
>
**Maximum valid score:**
>
> 100

## Possible Outputs
List all possible outputs of the program.
1. A correct, working program
2. A valid, not working program
3. A wrong program that interchanges score outputs
4. A program that has the right track but is still wrong
5. A program that is wrong entirely

## Boundary Condition
What condition will you use to determine whether the score is valid?
> 0-100

## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
> The program will identify your standing in your grades. It will tell you the classification you're in through the score you gave the program.
---
# Part 2 - Flowchart
Create a flowchart showing the logic of your program.
Your flowchart should show:
- Start
- Input score
- Valid score check
- Decision paths
- Classification
- Invalid score
- End

## Flowchart
### Insert your flowchart below.
>
[Score Checker Flowchart](score_checker_flowchart.png)
---

# Part 3 - Pseudocode
Create a pseudocode showing the logic of your program.

## Sample Pseudocode
>
START
>
INPUT score
>
IF score < 0 OR score > 100 THEN
>
DISPLAY "Invalid score."
>
ELSE IF score >= 90 THEN
>
DISPLAY "Outstanding"
>
....
>
END
## My Pseudocode

Module Main
>
Declare Integer score
>
Display "Give me your score:"
>
Input score
>
If score < 0 or score > 100 Then
>
Display "Invalid"
>
Else
>
If score >= 90 Then
>
Display "A"
>
Else
>
If score >= 80 Then
>
Display "B"
>
Else
>
If score >= 75 Then
>
Display "C"
>
Else
>
Display "D"
>
End If
>
End If
>
End If
>
End If
>
End Module

---
# Part 4 - Clean Code Implementation
## Source code
### Insert your source code.
>

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | | | |
| 2 | 0 | Minimum boundary | | | |
| 3 | 74 | Below Satisfactory boundary | | | |
| 4 | 75 | Satisfactory boundary | | | |
| 5 | 80 | Very Satisfactory boundary | | | |
| 6 | 90 | Outstanding boundary | | | |
| 7 | 100 | Maximum boundary | | | |
| 8 | 101 | Above maximum | | | |

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> Write your answers here
### 2. Why did you also test -1 and 101?
> Write your answers here
### 3. Which test helped you understand boundary conditions the most?
> Write your answers here
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> Write your answers here

---

# Reflection
### 1. How did selection structures make the program more useful?
> Write your answers here
### 2. How did proper comments and readable formatting improve your program?
> Write your answers here
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> Write your answers here
