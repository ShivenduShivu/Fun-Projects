import math
import time

def welcome():
    print('''
********************************************************************
            * Welcome to DO EASY interface *

# Refer us your choices :
    
To find prime numbers btw two numbers press '1'
   
To find factors of a given number press '2'

To find square root press '3'

For polynomial problems press '4'

To exit press '5'

''')
    exit

def operations():
    print("*" * 30)
    choice = int(input("Enter your choice : "))
    print("*" * 30)
    if choice == 1:
        prime_btw_two_numbers()

    elif choice == 2:
        factors()

    elif choice == 3:
        sqrt()

    elif choice == 4:
        polynomial()
        
    elif choice == 5:
        
        print("Thanks for using 'DO EASY'. Meet me for other help")
        exit

    else:
        print("Please make sure you choose from numbers 1,2,3,4,5")
        time.sleep(3)
        welcome()
        operations()
    

# code to find prime numbers between two digits

def prime_btw_two_numbers():
    t = 0
    while t == 0:
        
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))

        pno = []

        for i in range(num1, num2+1):
            for x in range(2,i):
                if i % x == 0:
                    break

            else:
                pno.append(i)


        print("The prime no's btw",num1, "&", num2,"are :",pno)

        print("Total no. = ",len(pno))

        t = int(input("To continue finding primes press '0' otherwise press '1' : "))
        if t == 1:
            welcome()
            operations()

# code to find factors of a given no.

def factors():
    t = 0
    while t == 0:
        
        num = int(input("Enter the number whose factor you want : "))

        factors = [1]

        for i in range(2,num+1):
            if num % i == 0:
                factors.append(i)


        print("The factors for ",num," are :",factors)

        print("Total factors = ",len(factors))

        t = int(input("To continue finding factors press '0' otherwise press '1' : "))
        if t == 1:
            welcome()
            operations()


# CODE TO FIND SQUARE ROOT OF A NUMBER

def sqrt():
    
    t = 0
    while t == 0:
        
        num = int(input("Enter the number whose sqrt you want : "))
        print("The sqrt. of ",num , " is ",math.sqrt(num))
        t = int(input("To continue finding factors press '0' otherwise press '1' : "))
        if t == 1:
            welcome()
            operations()

# CODE TO solve quadratic equations

def polynomial():

    t = 0
    while t == 0:
        
        from fractions import Fraction

        degree = int(input("Enter the degree of equation in digits(either 1,2,3) : "))

        if degree == 1:
            print("Please make sure equation is in the form 'ax + b = 0'")
            a = int(input("Enter the coefficient of 'x' : "))
            c = int(input("Enter the constant term : "))
            print("Your solution is : ",'(',Fraction(-c,a),')')
            t = int(input("To continue finding factors press '0' otherwise press '1' : "))
            if t == 1:
                welcome()
                operations()

        elif degree == 2:
            print("Please make sure equation is in the form 'ax^2 + bx + c = 0 ")
            a = int(input("Enter the coefficient of 'x^2' : "))
            b = int(input("Enter the coefficient of 'x' : "))
            c = int(input("Enter the constant term : "))

            d = b**2 - 4*a*c

            x = ((-b) + math.sqrt(d))/ (2*a)
            y = ((-b) - math.sqrt(d))/ (2*a)
            print("Your solutions are : ",'(',x,',',y,')')
            t = int(input("To continue finding factors press '0' otherwise press '1' : "))
            if t == 1:
                welcome()
                operations()
            
        
        elif degree == 3:
            
            print("Please make sure equation is in the form 'ax^3 + bx^2 + cx + d = 0 ")
            a = int(input("Enter the coefficient of 'x^3' : "))
            b = int(input("Enter the coefficient of 'x^2' : "))
            c = int(input("Enter the coefficient of 'x' : "))
            d = int(input("Enter the constant term : "))
            x =[]
            for i in range(-20,21):
                if (a*(i**3))+(b*(i**2))+(c*i)+d == 0:
                    x.append(i)

            print("Your solution for equation is : ",x)
            t = int(input("To continue finding factors press '0' otherwise press '1' : "))
            if t == 1:
                welcome()
                operations()



welcome()
operations()

