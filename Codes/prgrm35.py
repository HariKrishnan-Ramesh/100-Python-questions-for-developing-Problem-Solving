#Write a program to find the sum of all digits of a number n.
def sum_digits(n):
  sum = 0
  for i in n:
    sum += int(i)
  print(sum)

num = input("Enter the number: ")
sum_digits(num)