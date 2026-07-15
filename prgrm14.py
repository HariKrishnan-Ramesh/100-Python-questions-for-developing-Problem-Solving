#Program to find the smallest among the three numbers
def Comparenumbers(a, b, c):
  smallest = a
  if b < smallest:
    smallest = b
  if c < smallest:
    smallest = c
  print(f"{smallest} is the smallest number")

a, b, c = map(int, input("Enter three numbers to compare: ").split())
Comparenumbers(a,b,c)