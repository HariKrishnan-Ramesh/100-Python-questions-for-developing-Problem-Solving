#Write a program to find the product of all digits of a number n.
def sum_digits(n):
  prod = 1
  for i in n:
    prod *= int(i)
  print(prod)

num = input("Enter the number: ")
sum_digits(num)