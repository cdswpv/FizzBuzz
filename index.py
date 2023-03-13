#Function used to start python file and iterate through for loop
def main():
    for x in range (1, 101):
        FizzOrBuzz(x)
    return

#Function used to determine if Fizz, Buzz, Fizzbuzz, or the number should be printed
def FizzOrBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Calls function
main()
