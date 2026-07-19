#Write a program to find the largest digit in a number n.
def largest_digit(n):
  largest = 0
  for i in n:
    if i > str(largest):
      largest = i
  print(largest)

num = input("Enter the number: ")
largest_digit(num)