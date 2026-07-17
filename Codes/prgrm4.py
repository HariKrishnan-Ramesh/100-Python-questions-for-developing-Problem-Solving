#Program to read radius of a circle and print it's area and circumference.

def radius_circle(rad):
  print("Area of the circle:",3.14 * rad * rad)
  print("Circumference of the circle:",2 * 3.14 * rad)


rad = int(input("Enter the radius of the circle: "))
radius_circle(rad)