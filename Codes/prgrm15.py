import calendar

#Program to find wheather a year is leap year or not
def Leapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is leap year")
  else:
   print(f"The year {year} is not leap year")

year = int(input("Enter the year to check Leap year: "))
Leapyear(year)


# Another way
def Leapyear(year):
  if calendar.isleap(year):
    print(f"The year {year} is leap year")
  else:
   print(f"The year {year} is not leap year")

year = int(input("Enter the year to check Leap year: "))
Leapyear(year)