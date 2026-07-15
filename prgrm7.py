#Read value in celsius then into fareinheit

def Farenheit(temp):
  final_val = (temp - 32) * 5//9
  return final_val

temparature = int(input("Enter the temparature in Farenheit: "))
print(Farenheit(temparature),"celsius")