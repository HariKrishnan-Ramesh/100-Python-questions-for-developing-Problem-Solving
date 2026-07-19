#Write a program to reverse a number n.
def reverse_digits(n):
  rev = n[::-1]
  print(rev)

num = input("Enter the number: ")
reverse_digits(num)