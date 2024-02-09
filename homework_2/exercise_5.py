'''
Write a calculator program that takes two numbers and an operator (in str format), 
performs the given arithmetic operation and prints the result in the format: {num1} {operator) {num2) = {result}
'''
num_1 = int(input())
num_2 = int(input())
operator = input()
if num_2 == 0 and operator == '/':
      print("You can't divide by zero") 
elif operator == '+':
     result = num_1 + num_2
elif operator == '-':
     result = num_1 - num_2
elif operator == '/':
     result = num_1 / num_2
elif operator == '*':
     result = num_1 * num_2
print(f'{num_1} {operator} {num_2} = {result}')