#A list is a value that contains multiple values ina n ordered sequence. 
spam = ["Cat", "Dog", "Moose"]
print(len(spam))

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
random.shuffle(people)
print(people)
print(people[0])

helloworld = 'Hello,'
helloworld += ' world!'
print(helloworld)
bacon = ['Zophie']
bacon *= 3
print(bacon)

#Returns the index value of a list that contains 'hello'. 
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')

#list.append('') will add a new item to the end of the list. 
animals = ['cat', 'dog', 'bat']
animals.append('moose')
print(animals)

#list.insert(n, 'thing') will insert a new addition at index n of your list.
animals2 = ['cat', 'dog', 'bat']
animals2.insert(1, 'chicken')
print(animals2)

#list.remove('thing') will remove the first instance of the 'thing' in the list.
animals3 = ['cat', 'bat', 'rat', 'elephant']
animals3.remove('bat')
print(animals3)
#deleting a value not in a list will throw up an error. 

# del list[n] will remove the value at that index
animals4 = ['aardvark', 'ant', 'snake']
del animals4[2]
print(animals4)

# list.sort() will sort all integers in a list into ascending order.
# list.sort() will sort all strings in a list alphabetically. (Capitalized words will appear first. "Zebra" will show up before "aardvark")
numbers = [2, 3, 8, 0, -32, 190, 293, 2093, 1]
numbers.sort()
print(numbers)

words = ['dictionary', 'whore', 'bagel']
words.sort()
print(words)

# You can use True for the reverse keyword to have sort() sort in reverse.
words.sort(reverse=True)
print(words)

""" Practice Questions
1. What is []?
An empty array
2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam[2] = 'hello'

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to?
It will display spam[index value] of 3*2 // 11 which should be 0 which would be 'a' 
4. What does spam[-1] evaluate to?
'd'
5. What does spam[:2] evaluate to?
a & b

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
1
7. What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]
8. What does bacon.remove('cat') make the list value in bacon look like?
3.14, 11, 'cat', True

9. What are the operators for list concatenation and list replication?
+= & *=
10. What is the difference between the append() and insert() list methods?
Append adds it to the end, insert adds it to whatever index value you wish to assign it.
11. What are two ways to remove values from a list?
del and remove
12. Name a few ways that list values are similar to string values.

13. What is the difference between lists and tuples?
Tuples are immutable and can't be modified.
14. How do you type the tuple value that has just the integer value 42 in it?
tuple = ((42,))
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
tuple([]) and list(()) respectively
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
They contain references
17. What is the difference between copy.copy() and copy.deepcopy()?
copy.deeopcopy copies all lists in copied list. 

Practice Projects
For practice, write programs to do the following tasks:
Say you have a list value like this:
spam =['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function."""

def CommaConstructor(list):
    for i in :
