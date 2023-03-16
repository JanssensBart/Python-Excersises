'''
Exercise 4: Variables And Names

Now you can print things with print and you can do math. 
The next step is to learn about variables. In programming
a variable is nothing more than a name for something so you can use the name rather than the something as you
code.
Programmers use these variable names to make their code read more like English, and because they have lousy
memories. 
If they didn't use good names for things in their software, they'd get lost when they tried to read their code
again.

Jobs: 
    - use print(),use the variables and make it work ! :)

What You Should See :

$ python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.
$
 
'''

# Variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Your script below
