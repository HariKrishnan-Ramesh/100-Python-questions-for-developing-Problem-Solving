#Program to read length and breadth of rectangle and print it's area and perimeter

def Rectangle(length_val, breath_val):
  print("Area of the rectangle is: ", length_val * breath_val, "m/")
  print("Perimeter of the rectangle is: ", 2 * (length_val + breath_val))

length_val, breath_val = map(int, input("Enter the length and breadth: ").split())
Rectangle(length_val, breath_val)