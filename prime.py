number = int(input("Enter your number: "))
def prime_number(number):
    if (number % 2 == 0) and (number != 2):
        print ("Thats not prime number")
    elif  (number < 2):
        print ("Thats not prime number")
    else:
         print (" Thats prime number")
prime_number(number)
