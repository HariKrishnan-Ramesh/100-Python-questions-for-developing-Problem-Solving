#Program to print the all odd numbers from 1 to n 
def odd_num(n):
  for i in range(1, n+1):
    if i % 2 == 1:
      print(i, end=" ")

num = int(input("Enter the number: "))
odd_num(num)