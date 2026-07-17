#Program to read the mark of a student and print the Grade(A/B/C/Fail)
def graded_system(mark):
  if not 0 <= mark <= 100:
    print("Invalid Number")

  if mark <= 50:
    return "Fail"
  if mark <= 75:
    return "GRADE: C"
  if mark <= 90:
    return "GRADE: B"
  
  return "GRADE: A"


mark = int(input("Enter the mark: "))
print(graded_system(mark))