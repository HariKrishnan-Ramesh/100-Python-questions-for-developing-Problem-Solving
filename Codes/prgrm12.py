# Program to check wheather a number is POSITIVE, ZERO OR NEGATIVE

def numbertype(num):
  if num > 0:
    print("The number is positive.")
  elif num < 0:
    print("The number is negative.")
  else:
    print("The number is Zero.")

number = int(input("Enter the number:"))
numbertype(number)