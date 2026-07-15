#Program to check wheather given number is even or odd

def Evenorodd(num):
  if num % 2 == 0:
    print("The number is even")
  else:
    print("The number is odd")

number = int(input("Enter the number: "))
Evenorodd(number)