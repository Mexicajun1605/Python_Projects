#Collatz sequence


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        elif number % 2 != 0:
            number = 3 * number +1
            print(number)
        
collatz(int(input('Please input any number you would like to receive its Collatz sequence.\n')))