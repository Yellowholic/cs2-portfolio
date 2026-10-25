def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3 

def get_performance(average):
  if average >= 85:
     return "Mastery"
  elif average >= 70:
     return "Developing"
  else:
     return "Needs Review"

def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return True
  else: 
    return False 

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))
score3 = float(input("Enter the third score: "))
completed_tasks = int(input("Enter how many tasks have been completed: "))

average = calculate_average(score1, score2, score3)
print("Average: ", average)

performance = get_performance(average)

eligible = is_eligible(average, completed_tasks)
print("Eligible for challenge:", eligible)

# Documentation questions

# 1. Which function returns a number, which returns a string, and which returns a Boolean?
#     - The calculate_average() function returns a number, get_performance() returns a string, and is_eligible() returns a Boolean.
# 2. Explain how the average moves from calculate_average() into get_performance().
#     - The program saves the value returned by calculate_average() into a variable and then passes that variable directly into get_performance().
# 3. What happens when a student has a high average but has completed fewer than three tasks?
#     - The program will evaluate the student as ineligible fpr the challenge and return False because both conditions must be met.
# 4. Why is return more appropriate than simply printing the result inside each function?
#     -Using return sends data back to the program so it can be reused by other functions, whereas printing only displays text on the screen.
