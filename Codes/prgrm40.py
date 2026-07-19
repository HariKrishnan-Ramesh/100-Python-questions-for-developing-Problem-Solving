# Write a program to count the number of even digits and odd digits in a number n.
def evenodd_digit(n):
    even = 0
    odd = 0
    for digit in n:
        digit = int(digit)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"even = {even}, odd = {odd}")

num = input("Enter the number: ")
evenodd_digit(num)