'''
Facts:
Prime numbers are greater than 1
Prime numbers are only divisible by itself and 1
'''
num = int(input("Enter a number: "))

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print("%d is not a prime number" % (num))
            print("{} times {} is {}".format(i, num//i, num))
            break
    else:
        print(f"{num} is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(f"{num} is not a prime number")
