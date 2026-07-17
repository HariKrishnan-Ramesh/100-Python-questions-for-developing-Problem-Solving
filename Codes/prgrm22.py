#Program to print the all natural numbers from 1 to n in reverse order
def count_reverse(n):
  for i in range(n, 0, -1):
    print(i, end=" ")

num = int(input("Enter the number for reverse: "))
count_reverse(num)