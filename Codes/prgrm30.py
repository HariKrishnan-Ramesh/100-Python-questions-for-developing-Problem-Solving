#program to display all multiples of number M upto N terms
def multiples_num(n):
  s=[]
  for i in range(1, n+1):
    if i * (i+1) == n:
      print(1, i, (i+1), n)
      

      


num = int(input("Enter the number to find the multiples: "))
multiples_num(num)