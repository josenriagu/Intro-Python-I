import os

# clear console before operation
clear = lambda: os.system('cls')
clear()

def sieveOfErathosthenes(*args):
    '''
    Stretch thoughts:
    - Allow for arbitrary number of values
    - If start value is greater than end? return a message
    - If one argument is passed, use as end value and set start to 0
    '''
    # initialize variables
    start = 0
    end = 0
    if len(args) >= 2:
        start = args[0]
        end = args[1]
        if start > end:
            print("Hollup! start value should be less than end value")
            return
    elif len(args) == 1:
        end = args[0]
    '''
    - From this line solves the basic instance where our function is given two required arguments
    '''
    # initialise a list to hold our primes
    primes = []
    # iterate between start and end
    for el in range(start, end + 1):
        if el == 0 or el == 1:
            continue
        elif el == 2 or el == 3 or el == 5 or el == 7:
            primes.append(el)
        elif el % 2 == 0 or el % 3 == 0 or el % 5 == 0 or el % 7 == 0:
            continue
        else:
            primes.append(el)
    
    print() # print empty space for demarcation
    print("There are {} prime numbers between {} and {} as shown in the array below: ".format(len(primes), start, end), primes, sep="\n")
    print() # print empty space for demarcation

sieveOfErathosthenes(120)
sieveOfErathosthenes(2, 120)
sieveOfErathosthenes(2, 120, 5)
sieveOfErathosthenes(150, 120, 5)
