#Swap a value without any third variable

def swap_var(a, b):
  print("Value of A & B before swapping a=",a, "b =", b)
  a, b = b, a
  print("Value of A & B after swapping a=",a, "b =", b)
  
a, b = map(int, input("Enter the A and B: ").split())
swap_var(a, b)

