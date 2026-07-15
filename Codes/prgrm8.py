#Swap a value without any third variable

def Swapvariable(a, b):
  print("Value of A & B before swapping a=",a, "b =", b)
  a, b = b, a
  print("Value of A & B after swapping a=",a, "b =", b)
  
a, b = map(int, input("Enter the A and B: ").split())
Swapvariable(a, b)

