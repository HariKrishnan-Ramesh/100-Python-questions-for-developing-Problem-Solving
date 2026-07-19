#Write a program to find the product of all digits of a number n.
def product_digits(n):
  prod = 1
  for i in n:
    prod *= int(i)
  print(prod)

num = input("Enter the number: ")
product_digits(num)