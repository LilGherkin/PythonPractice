# This is a comment, and won't be displayed, or cause an error. 
# """ Allows us to make a fake multiline comment. It's technically a string, but it won't be printed.
# There is no way to make a multiline comment as there is in JavaScript. 
# But you can just keep doing this. 


# Print is how we get Python to print our message to the command line. 
print ("Hello, world!")

# We can perform math, same as we can in any other language.
# +, -, *, / are for: addition, subtraction, multiplication, and division respectively.
# **, %, // are for: exponents, modulus, and division rounded down respectively.
print(3+3, 3-3, 3*3, 3/3, 3**3, 3%2, 3//2)
# Running the previous command we see that 3/3 produces 1.0 instead of just 1. It is evaluating to a float as oppossed to an integer. 

# We can + strings together to combine them. 
print('Alice is ' + 'fighting.')

# We cannot perform mathmatic operations on strings and integers, as it runs into an error.
# We can however use * on a string and an int to have it display the same string multiple times.
print('fold' * 5)

# We can assign variables to store a single value, and then refer to it with that variable later on. 
test = 42

print(test)

# We can assign and then reassign variables to overwrite their values.
aloha = "Hello"
print(aloha)
aloha = "Goodbye"
print(aloha)

# You can name a variable anything so long as it:
# * Only one word with no spaces.
# * Can only use letters, numbers, and underscores.
# * It cannot start with a number. 
# Variable names are case sensative. So Var1 is seperate from var1. It is traditional to start variables with lowercase letters, and utilize camalCase.

# Let's make a quick program.

# This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?') # This is an inline comment and won't be printed. We'll need to ask for their name.
myName = input() #input() prompts the user to enter in a piece of information. myName then stores that information so we can use it later.
print("It's good to meet you, " + myName + '.')
print('The length of your name is: ' + str(len(myName)) + ' characters.') #len() evaluates the number of characters in a string.
print("How old are you?") #Prompt them for their age.
myAge = input()
print("You'll be " +str(int(myAge)+1) + " on your next birthday.")

# Practice Questions
# 1. Which of the following are operators, and which are values?

#1: *
#2: 'hello'
#3: -88.8
#4: -
#5: /
#6: +
#7: 5

# Answer: 1, 4, 5, 6 are operators. 

# 2. Which of the following is a variable, and which is a string?

# spam
# 'spam'

# Answer: spam is a variable. 'spam' is a string.

# 3. Name three data types.

# Answer: float, integer, string, boolean is another.

# 4. What is an expression made up of? What do all expressions do?

# Answer: An expression is any set of n>=2 values with n>=1 operators that results in returning one value. 

# 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

# Answer: A statement is literally just a statement like 'ring', an expression has an end value.

# 6. What does the variable bacon contain after the following code runs?

#bacon = 20
#bacon + 1

# Answer: Bacon will still contain a value of 20. Adding 1 to it is just asking the computer 20 + 1 = ?. 

# 7. What should the following two expressions evaluate to?

# 'spam' + 'spamspam'
# 'spam' * 3

# Answer: They'll both evaluate to 'spamspamspam'

# 8. Why is eggs a valid variable name while 100 is invalid?

# Answer: Variables cannot start with numbers.

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# Answer: int(), flt(), str().

# 10. Why does this expression cause an error? How can you fix it?

# 'I have eaten ' + 99 + ' burritos.'

# Answers: It produces an error becuase 99 is an int, and it doesn't know how to add a str and an int together. It can be fixed by adding apostrophes around the 99, or by doing str(99).

# Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.

print(round(43.5))

# Answers: round() will round a float to the nearest whole integer. 