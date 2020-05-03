# The script must be run with python 3

while True:
    try:
        num = int(input('Enter a number in order to generate the sequence: '))
    except:
        print("Invalid input.....try again")
        continue
    else:
        # Breaks the loop when a valid input is entered
        break


# Functipn to generate the sequence
def sequenceGenerator(num):
    a = 0
    b = 1
    if num <= a:
        print("Please a enter a valid input")
    elif num == b:
        print(0)
    elif num > 1:
        print("The sequence is " + "{},{}".format(a,b), end='')
        for i in range(2, num):
            c = a+b
            print(",{}".format(c), end='')
            a=b
            b=c


sequenceGenerator(num)