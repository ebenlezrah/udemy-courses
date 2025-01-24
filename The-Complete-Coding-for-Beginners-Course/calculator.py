def addition(number_1,number_2):
  return number_1+number_2

def subtraction(number_1,number_2):
  return number_1-number_2

def multiplication(number_1,number_2):
  return number_1*number_2

def division(number_1,number_2):
  return number_1/number_2

x = True
while x:
  print("Give me 2 numbers and an operation type (+,-,*,/) to make a calculation")
  number_1 = float(input("Number 1: "))
  number_2 = float(input("Number 2: "))
  operation = int(input("Operation (+=1,-=2,*=3,/=4): "))

  if operation == 1:
    print(addition(number_1,number_2))
    x = False
  elif operation == 2:
    print(subtraction(number_1,number_2))
    x = False
  elif operation == 3:
    print(multiplication(number_1,number_2))
    x = False
  elif operation == 4:
    if number_2 == 0:
      print("Cannot divide by zero. Try again\n")
    else:
      print(division(number_1,number_2))
      x = False
  else:
    print("Invalid input. Try again\n")