#program to print the multiplication table of n:
def mul_table(n):
  for i in range(1, 11):
    print(f"{i} x {n} = {i*n}")

num = int(input("Enter the number for multiplication table: "))
mul_table(num)