# Write a program to print sum, difference, product and quotient

def Arithemetic(a, b):
  print("Sum:",a+b)
  print("Product:",a*b)
  print("Quotient:",a//b)

a, b = map(int, input("Enter the numbers: ").split())
Arithemetic(a, b)