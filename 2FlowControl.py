# Boolean values are values that equate to either True or False. 
booleanexample1 = True
booleanexample2 = False

# Python has comparision operators that will output as True or False.
# == equal to. 42 == 42 outputs 2. 41 == 42 outputs false.
# != not equal to. 42 != 41 outputs true. 42 != 42 is false.
# < less than. 42 < 43 is true. 42 < 41 is false.
# > greater than. 42 > 41 is true. 42 > 43 is false.
# <= less than or equal to. 42 <= 42 is true. 42 <= 41 is false.
# >= greater than or equal to. 42 >= 42 is true. 42 >= 43 is false. 

# == & != can work for any data type including strings. "Hello" == "Hello" is true. "Hello" == "hello" is false due to case sensitivity.
# == cannot work between strings and ints/floats, but == can work between floats and ints. 
# != would work mostly as intended between strings and ints/floats

print(42==42.0) #This will evaluate to true as both are numbers. 
print('42'==42) #This will evaluate to false becase '42' is different from 42. 

# Boolean operators exist. They are AND, OR, and NOT.
# AND evaluates to true if all parts of the expression are true. 
## True AND True = True. True AND False = False.
# OR evalautes to true if at least one of the parts of the expression are true.
## True OR True = True, True OR False = True, False OR False = False
# NOT inverts whatever the end result is.
## NOT True = False, NOT False = True. 
## NOT operators can be nested. NOT NOT True = True. 

# We can use comparison operators and boolean operators in conjunction with one another. 
print((5 > 3) and (5 >2))

# Flow control statements often start with a part called the condition and are always followed by a block of code called the clause.
# Conditions always evaluate down to a Boolean value, True or False. 
# A flow control statement decides what to do based on whether its condition is True or False.
# Almost every flow control statement uses a condition.

# Lines of Python code can be grouped together in blocks. 
# You can tell when a block begins and ends from the indentation of the lines of code. 
# There are three rules for blocks.
## Blocks begin when the indentation increases.
## Blocks can contain other blocks.
## Blocks end when the indentation decreases to zero or to a containing block’s indentation.

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# If statements are a form of flow control. If the condition is met, then execute the following line, otherwise, skip it. 
# else is to be executed if the evaluation at the if statement is false. if x is true do y, else do z. 
# elif is to be included in things where we have multiple cases, with the else acting as a catch all. 
## if name == 'mary' do x, elif name == 'sue' do y, else do z.

name = 'Carol' # Set our name to Carol
age = 3000 # Set our age to 3000
if name == 'Alice': # Is our name == 'Alice'. No, it's Carol. We'll skip this block.
    print('Hi, Alice.') # Skipped
elif age < 12: # Is our age < 12? No, we're 3000. Skip this block.
    print('You are not Alice, kiddo.') # Skipped.
elif age > 2000: # Is our age > 2000? Yes, we're 3000, we'll execute this block.
    print('Unlike you, Alice is not an undead, immortal vampire.') # Print this line.
elif age > 100: # We've already hit our first true statement, so this will get skipped even though it is true as well. 
    print('You are not Alice, grannie.') # Skipped.

# We can swap the age blocks, and get a different print out. 

name = 'Carol' # Set our name to Carol
age = 3000 # Set our age to 3000
if name == 'Alice': # Is our name == 'Alice'. No, it's Carol. We'll skip this block.
    print('Hi, Alice.') # Skipped
elif age < 12: # Is our age < 12? No, we're 3000. Skip this block.
    print('You are not Alice, kiddo.') # Skipped.
elif age > 100: # Is our age > 100? Yes, we're 3000, we'll execute this block.
    print('You are not Alice, grannie.') # Print this line. 
elif age > 2000: # We already hit a true condition. So this is skipped.
    print('Unlike you, Alice is not an undead, immortal vampire.') # Skipped.

# We don't have any else statements in this block. So if we were to change our age to somewhere between 12 and 100, it would error out. 
# We can set it up with an else statement that serves as a catch all. 

name = 'Carol'
age = 75
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

# WHILE Loops
# We can set a loop that continues to run until something causes it to stop. 
counter = 0
while counter < 5:
    print("Hello, world!")
    counter = counter + 1
# The above will print out Hello world 5 times, counter keeps getting overwritten with a new number until counter < 5 = false. 

# We can set up an annoying while loop that doesn't break until you set your name to 'your name'
name = '' #blank out our name variable since we use it in our previous examples.
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you.') 

# Assuming we never figured out that name needs to be your name, we would be trapped there until we figured it out.
# We can do the same thing, except we can theoretically trap someone forever.
# We can use the following code to create an infinite loop. The only thing that saves someone is by typing your name to trigger a break.
# If the break werent' there, no matter what they typed in, they'd be stuck.
# Break takes escapes you from the current block.
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you.')

# A true infite loop can be broken by hitting CTRL + C in the command prompt. Uncomment the following 2 lines to test it.
# while True:
#    print('Hello, world!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. Please enter your password.')
    password = input()
    if password == 'Barricuda':
        break
print('Access granted')

# Continue is similar to break, except we tell it to essentially skip whatever use case we hit. For example if we have a divid by 0
# we can use continue to essentially keep running the loop, but know that if we hit 0 we need to skip over it. 

# FOR loops
# For each item in a list do the following.
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

# You can use a while loop in place of a for loop some times such as in the following:
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# Some functions can take in multipe arguments. range() is one of them. We can call range(x y z) x = starting value y = end z = interval.
# range(0, 10, 2) Will get every number from 0-10 and increments by 2 so we'll see 0, 2, 4, 6, 8.
for i in range(0, 10, 2):
    print(i)

# We can use this functionality to count down as well. The following will print out 5, 4, 3, 2, 1, 0.
for i in range(5, -1, -1):
    print(i)

# We can import modules into python to perform functiosn outside of basic python's scope. 
# We call these with 'import' along with the module name. 
# The following calls the random module white 
import random
for i in range(5):
    print(random.randint(1,10))

# We can import multiple modules by separating them with commas as seen in the following example.
import random, sys, os, math