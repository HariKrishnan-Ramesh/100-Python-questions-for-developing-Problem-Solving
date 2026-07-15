#Program to read seconds and convert them into HOURS, MINUTES AND SECONDS.....

seconds = int(input("Enter the seconds:"))
hours = seconds/3600
minutes = seconds/60
seconds = seconds
print("The time is:",hours,"Hours",minutes, "Minutes" ,seconds, "seconds")
