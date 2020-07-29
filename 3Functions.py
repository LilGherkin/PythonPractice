# You can make functions with the def() command
def hello():
    print("Howdy!")
    print("What's up?")
    print("Hello there!")
hello()
#We defined the hello function above to print out 3 lines, and then call it, and it prints all 3 lines. 

#Functions with Parameters
#As seen above we can call a function, but we can also add a parameter that gets entered into it when we call it.
def hello2(name):
    print("Hello " + name)
hello2('Alice')
hello2('Bob')