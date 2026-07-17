#Program to print the sum of all odd numbers from 1 to n 
def sum_oddnum(n):
  sum = 0
  for i in range(1, n+1):
    if i % 2 == 1:
      sum += i
  print("Total sum of odd number is:", sum)

num = int(input("Enter the number: "))
sum_oddnum(num)