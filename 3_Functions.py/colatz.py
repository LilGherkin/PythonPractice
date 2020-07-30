import sys
def colatz(number):
    if number == 1:
        sys.exit()
    elif number % 2 == 0:
        result = number // 2
        print(result)
        colatz(result)
    else: 
        result = (3 * number + 1)
        print(result)
        colatz(result)


try:
    number = int(input("Enter a number: "))
    colatz(number)
except ValueError:
    print("Please enter an integer.")

