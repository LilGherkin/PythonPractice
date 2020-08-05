"""
Comma Code
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
"""
grocery= ["Ham"]
grocery2 = ["Ham", "Cheese"]
grocery3 = ["Ham", "Egg", "Cheese"]

def fuctional(listicle):
    if len(listicle) == 0:
        print("Please provide a valid list")
    elif len(listicle) == 1:
        print(listicle[0])
    else:
        for i in range(len(listicle) - 1):
            print(listicle[i] + ', ', end='')
        print('and ' + listicle[i + 1])

fuctional(grocery)
fuctional(grocery2)
fuctional(grocery3)

customlist = []
while True:
    item = input('Please enter an item for your list or press enter to stop.\n')
    if item is not '':
        customlist.append(item)
    else:
        break
fuctional(customlist)