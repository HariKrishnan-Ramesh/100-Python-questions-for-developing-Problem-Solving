#Program to find the largest among three numbers
def compare_num(a,b,c):
  greatest = a
  if b > greatest:
    greatest = b
  if c > greatest:
    greatest = c
  print(f"{greatest} is the largest number")

a, b, c = map(int, (input("Enter the three inputs to be compared:")).split())
compare_num(a,b,c)