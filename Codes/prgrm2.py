def sum_numbers(num1, num2):
  return (num1 + num2)


num1, num2 = map(int, input("Enter the numbers to find the sum: ").split())
print(sum_numbers(num1, num2))