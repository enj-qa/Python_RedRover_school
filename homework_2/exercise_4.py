# Write a program that prints the input text a given number of times, line by line. The text and the number of repetitions should be entered using input()
text_from_user = input('Please, enter your text here - ')
repetitions_text = int(input('Please, enter num of repeat your text - '))
for i in range(repetitions_text):
    print(text_from_user)