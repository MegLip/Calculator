import logging

def add (num1, num2):               #1 def function
    return num1 + num2
def add (num1, num2, *args):               
    return num1 + num2 + sum(args)  
def substract (num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def multiply (num1, num2, *args):
    x = 1
    for num in args:
        x *= num
        y = x * num2 * num1
    return(y)
def divide (num1, num2):
    return num1/num2

print("Podaj działanie, posługując się odpowiednią liczbą:" '\n' "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")        #2 choice operation
choice = input("Podaj numer działania (1,2,3,4): ")
