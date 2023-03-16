'''
Exercise 6: “New Style” String Formatting (str.format)

JOBS :
    - run the script : python3 ex6.py
    - Try to create you own sentences !
    - @info : (ctrl+click)
    https://realpython.com/python-string-formatting#2-new-style-string-formatting-strformat
 
'''

# code
x = "There are {} types of people.".format(2)
binary = "binary"
do_not = "don't"
y = f'Those who know {binary} and those who {do_not}.'

print(x)
print(y)

print(f'I said: {x}')
print(f"I also said: {y}")

hilarious = False
joke_evaluation = f"Isn't that joke so funny?! {hilarious}"

print(joke_evaluation)

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
