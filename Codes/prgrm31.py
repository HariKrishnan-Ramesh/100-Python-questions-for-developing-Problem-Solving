#Program to count how many numbers from 1 to n are divisible by 3
def count_num(n):
  count = 0
  for i in range(1, n+1):
    if i % 3 == 0:
      count += 1
  print(count)


num = int(input("Enter the Number: "))
count_num(num)