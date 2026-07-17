#Read value in celsius then into fareinheit

def farenheit(temp):
  final_val = (temp - 32) * 5//9
  return final_val

temparature = int(input("Enter the temparature in Farenheit: "))
print(farenheit(temparature),"celsius")