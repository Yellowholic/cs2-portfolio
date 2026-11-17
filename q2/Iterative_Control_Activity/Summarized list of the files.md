# Iterative Control Activity Summary

This repository contains four Python scripts demonstrating basic iterative control structures (`for` loops, `while` loops, `continue` statements, and functions).

---

## 1. Count Even Numbers (`Count_Even_Numbers.py`)
**Goal:** Print all even numbers from 2 to 20.

### Code
- [Count_Even_Numbers.py](q2/Iterative_Control_Activity/Count_Even_Numbers.py)

### How It Works
* Uses a `for` loop with the `range(start, stop, step)` function.
* Starts at `2`, stops before `21` (so `20` is included), and increments by `2` on each iteration.

---

## 2. The Countdown Timer (`The_Countdown_Timer.py`)
**Goal:** Count down from 10 to 1 and display a message when finished.

### Code
- [The_Countdown_Timer.py](q2/Iterative_Control_Activity/The_Countdown_Timer.py)

### How It Works
* Initializes `count` at `10`.
* Repeats the `while` loop as long as `count` is greater than or equal to `1`, printing the current number and subtracting `1` each time.
* Exits the loop once `count` reaches `0` and prints `"Time is up!"`.

---

## 3. Skip Multiples (`Skip_Multiples.py`)
**Goal:** Print numbers from 1 to 15 while skipping multiples of 3.

### Code
- [Skip_Multiples.py](q2/Iterative_Control_Activity/Skip_Multiples.py)

### How It Works
* Loops through numbers `1` to `15` using `range(1, 16)`.
* Checks if `num` is divisible by `3` using the modulo operator (`%`).
* Uses `continue` to skip the `print()` statement whenever a multiple of 3 is found.

---

## 4. Multiplication Table Generator (`Multiplication_Table_Generator.py`)
**Goal:** Ask the user for a number and display its multiplication table from 1 to 10.

### Code
- [Multiplication_Table_Generator.py](q2/Iterative_Control_Activity/Multiplication_Table_Generator.py)

### How It Works
* Defines a function `show_table(number)` that loops from `1` to `10` (`range(1, 11)`) and prints each multiplication step.
* Prompts the user for an integer input outside the function and passes it into `show_table()` to generate the output.

###### Credits to Gemini for helping me summarize all of my codes into a .md file
