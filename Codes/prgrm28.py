#Program to find the factorial of a num
def product_num(n):
  prod = 1
  for i in range(1, n+1):
    prod = prod * i
  print(prod)

num = int(input("Enter the number: "))
product_num(num)