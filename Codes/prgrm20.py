#Program to check wheather a person is eligible to vote
def vote_elg(age):
  if age > 18:
    return "Eligible for Voting"
  else:
    return "Not Eligible" 

age = int(input("Enter the age: "))
print(vote_elg(age))