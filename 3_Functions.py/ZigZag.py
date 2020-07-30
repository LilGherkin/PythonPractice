#Other modules created by other people so we don't have to make a system to measure time.
import time, sys
indent = 0 #How many spaces the zig zag is indented, at 0 to start
indentIncrease = True #Whether or not to increase our indentation.

try:
    while True: # As long as it is true, do the following
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
    
        if indentIncrease:
            #Increases the number of indent
            indent = indent + 1
            if indent == 20:
                #Change direction
                indentIncrease = False
        
        else:
            #Decreaes the number of spaces
            indent = indent - 1
            if indent == 0:
                #Change direction
                indentIncrease = True

except KeyboardInterrupt:
    sys.exit()