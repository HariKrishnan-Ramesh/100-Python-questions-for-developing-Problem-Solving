#Program to read a character and check wheather it's a vowel or not
def Isvowel(strg):
  if strg in "aeiou":
    print(f"{strg} is a vowel")
  else:
    print(f"{strg} is not a vowel")

string = input("Enter the string: ")
Isvowel(string)

#We can use is.alpha() built-in function to check wheather a program vowel or not, But try to do using without it. While doing in a production it's always best to use the BUILT-IN Functions. While developing your logic and methods it's good to use the other ways.