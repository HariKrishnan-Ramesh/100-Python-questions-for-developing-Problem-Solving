#Write a program to find the smallest digit in a number n.
def smallest_digit(n):
  smallest = n
  for i in n:
    if i < str(smallest):
      smallest = i
  print(smallest)

num = input("Enter the number: ")
smallest_digit(num)