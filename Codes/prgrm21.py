#Program to print the all natural numbers from 1 to n
def count_num(n):
  for i in range(1, n+1):
    print(i, end=" ")

num = int(input("Enter the number: "))
count_num(num)