#program to display all multiples of number M upto N terms
m = int(input("Enter the number (m): "))
n = int(input("Enter the number of terms (n): "))

print(f"The first {n} multiples of {m} are:")
# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    print(m * i, end=" ")
