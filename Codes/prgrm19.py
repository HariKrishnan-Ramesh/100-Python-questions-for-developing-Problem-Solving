#Program to read a number and check it is divisible by 3 and 5
def check_num(num):
  if (num % 3 == 0 and num % 5 == 0):
    print("Number is divisible by 3 and 5")
  else:
    print("Number is not satisfied!")

num = int(input("Enter the number: "))
check_num(num)