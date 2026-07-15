#Program to read a mark of 5 subjects print there total and average


sub1 = int(input("Enter the value of First Subject: "))
sub2 = int(input("Enter the value of Second Subject: "))
sub3 = int(input("Enter the value of Third Subject: "))
sub4 = int(input("Enter the value of Fourth Subject: "))
sub5 = int(input("Enter the value of Fifth Subject: "))


Total = sub1 + sub2 + sub3 + sub4 + sub5 
Avg = Total/5
print("The Total of the 5 subjects are: ", Total)
print("The Average of the 5 subjects are: ", Avg)
