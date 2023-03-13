def main():
    for x in range (1, 101):
        FizzOrBuzz(x)
    return

def FizzOrBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


main()
