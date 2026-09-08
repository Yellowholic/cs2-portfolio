score = int(input("Enter the score: "))

if score < 0 or score > 100:
  print("Invalid")

elif score >= 90:
  print("Your grade is A")

elif score >= 80:
  print("Your grade is B")

elif score >= 75:
  print("Your grade is C")

else:
  print("Your grade is D")
