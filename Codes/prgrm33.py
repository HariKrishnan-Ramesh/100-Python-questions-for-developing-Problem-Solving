#Write a program to count the number of digits in a number N.
def count_digits(n):
  count=0
  for i in n:
    count += 1
  print(count)

num = input("Enter the number: ")
count_digits(num)
