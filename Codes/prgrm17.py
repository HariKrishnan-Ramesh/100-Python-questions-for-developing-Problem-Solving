#Program to check wheather if it's alphabet digit or special symbol
def IsCharacter(char):
  if char.isalpha():
    print("The character is an Alphabet")
  elif char.isdigit:
    print("The character is a Digit")
  else:
    print("The character is a Sprcial Character")

character = input("Enter the CHARACTER: ")
IsCharacter(character)