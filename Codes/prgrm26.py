#Program to print the sum of all evem numbers from 1 to n 
def sum_evnum(n):
  sum = 0
  for i in range(1, n+1):
    if i % 2 == 0:
      sum += i
  print("Total sum of even number is:", sum)

num = int(input("Enter the number: "))
sum_evnum(num)