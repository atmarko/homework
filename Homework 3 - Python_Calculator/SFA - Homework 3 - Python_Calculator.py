# Define a method for addition
def add(x,y):
    z = x + y
    return z

# Define a method for subtraction
def subtract(x,y):
    z = x - y
    return z

# Define a method for multiplication
def multiply(x,y):
    z = x * y
    return z

# Define a method for division
def divide(x,y):
      z = x / y
      return z
   
     
# Loop for checking the desired calculation if the input is valid
while True:

  print ('Please specify the desired calculation (1-add,2-subtract,3-multiply,4-divide)')
  calculation = input()

  while calculation < '1' or calculation > '4':
  
    print('Would you like to re-run the calculator and enter a valid operation (1-add,2-subtract,3-multiply,4-divide) \n Please enter y or n')
    answer = input()
    if answer != "y":
      exit()
  
    else:
      print ('Please specify the desired calculation (1-add,2-subtract,3-multiply,4-divide)')
      calculation = input()

  
  print('Please enter 2 numbers for the desired calculation \nPlease enter the first number')
  x = input()
  try:  
    x = float(x)
  except ValueError:
    # Look for checking if input is a valid (float or int)
    while isinstance(x, (float, int)) == False:
      # Try to convert the input to a float
      try:  
        x = float(x)
      except ValueError:
  # Ask for an input
        print('Please enter a valid number') 
        x = input()
        
        
  print('Please enter the second number')
  y = input()
  try:  
    y = float(y)
  except ValueError:
    while isinstance(y, (float, int)) == False:
      # Try to convert the input to a float
      try:  
        y = float(y)
      except ValueError:
  # Ask for an input
        print('Please enter a valid number') 
        y = input()

  # Check the desired calculation and print the result
  if calculation == '1':
    print(x, '+', y, '=', add(x,y))
    print(x, '+', y, '=',"{:.2f}".format(add(x,y)))
    print(x, '+', y, '=',"{:.3f}".format(add(x,y)))
    print(x, '+', y, '=',"{:.4f}".format(add(x,y)))
  elif calculation == '2':
    print(x, '-', y, '=', subtract(x,y))
    print(x, '+', y, '=',"{:.2f}".format(subtract(x,y)))
    print(x, '+', y, '=',"{:.3f}".format(subtract(x,y)))
    print(x, '+', y, '=',"{:.4f}".format(subtract(x,y)))
  elif calculation == '3':
    print(x, '*', y, '=', multiply(x,y))
    print(x, '+', y, '=',"{:.2f}".format(multiply(x,y)))
    print(x, '+', y, '=',"{:.3f}".format(multiply(x,y)))
    print(x, '+', y, '=',"{:.4f}".format(multiply(x,y)))
  else:
    calculation == '4'
  if y!=0:
    print(x, '/', y, '=', divide(x,y))
    print(x, '+', y, '=',"{:.2f}".format(divide(x,y)))
    print(x, '+', y, '=',"{:.3f}".format(divide(x,y)))
    print(x, '+', y, '=',"{:.4f}".format(divide(x,y)))
  else:
    print('Error: Cannot divide by zero')
  
  print('Would you like to proceed with a new calculation? \n Please enter y or n')
  if input() != "y":
    exit()
