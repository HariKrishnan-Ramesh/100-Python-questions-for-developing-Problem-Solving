#Program to print the all even numbers from 1 to n 
def even_num(n):
  for i in range(1, n+1):
    if i % 2 == 0:
      print(i,end=" ")

num = int(input("Enter the number: "))
even_num(num)