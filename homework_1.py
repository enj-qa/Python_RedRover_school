#1) Write and run a program that outputs the string "Hello world!" 
print("Hello world!")

#2) Write a program that takes a user name as input, stores it in the user_name variable, and outputs the string "Hello {user_name}!" 
name_user = input() + '!'
print('Hello', name_user)

#3) Write a program that takes 2 numbers as input, performs an arithmetic operation on them (at your discretion), and outputs "Result = {result}".
first_num = int(input())
second_num = int(input())
print('Result =', first_num + second_num)

"""
4) Write a program to output:     
*********
*       *
*       *
*********

"""

print('*' * 9)
print('*', '*', sep= 7 * ' ')
print('*', '*', sep= 7 * ' ')
print('*' * 9)

#5 Write a program to find the digits of a four-digit number. The number is entered using the input() method
num_from_user = int(input())
Thousands_num = num_from_user // 1000
Hundreds_num = num_from_user // 100 % 10
Tens_num = num_from_user % 100 // 10
Units_num = num_from_user % 10
print('Thousands of num is -', Thousands_num)
print('Hundreds of num is -', Hundreds_num)
print('Tens of num is -', Tens_num)
print('Units of num is -', Units_num)

#6 Write a program that reads two integers a and b and displays the square of the sum of (a+b)2 and the sum of the squares a2+b2 of these numbers.
a, b = int(input()), int(input())
square_of_sum = (a + b)**2
sum_of_squares = a**2 + b**2
print('The square of the', a, 'and', b, '=', square_of_sum)
print('The sum of the squares', a, 'and', b, '=', sum_of_squares)
