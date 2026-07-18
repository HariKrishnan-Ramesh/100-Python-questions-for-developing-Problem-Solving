#Program to display all numbers from 1 to N divisible by 3 and 5
def divisible_num(n):
  for i in range(1, n+1):
    if (i % 3 == 0 and i % 5 == 0):
      print(i)


num = int(input("Enter the number: "))
divisible_num(num)