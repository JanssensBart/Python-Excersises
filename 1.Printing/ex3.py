'''
Exercise 3: Numbers And Math

This exercise has lots of math symbols. Let's name them right away so you know what they are called. As you type
this one in, say the names. When saying them feels boring you can stop saying them. 

Here are the names:
• + plus
• - minus
• / slash
• * asterisk
• % percent
• < less-than
• > greater-than
• <= less-than-equal
• >= greater-than-equal

JOBS:
    - run python3 ex3.py
    - Look at the syntax and try them out in bash mode!

What You Should See:

$ python ex3.py
I will now count my chickens:
Hens 30
Roosters 97
Now I will count the eggs:
7
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
$   
'''

print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
