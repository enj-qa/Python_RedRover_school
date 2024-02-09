'''
Write a program that checks if a year is a leap year. 
Years that are divisible by 4 without a remainder (2004, 2008) and are not centuries (500, 600) are considered leap years. 
However, if a year is divisible by 400, it is also considered a leap year (1200, 2000)
'''
num_year = int(input('Please enter number of year - '))
if num_year > 0:
    if (num_year % 4 == 0 and num_year % 100 != 0) or num_year % 400 == 0:
        print('This year is a leap - ', num_year)
    else:
        print('This is not a leap year -', num_year)
else:
    print('Enter positive num of year, please!')
