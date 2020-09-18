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
    return num1 * num2 * sum(args)   
def divide (num1, num2):
    return num1/num2

print("Podaj działanie, posługując się odpowiednią liczbą:" '\n' "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")        #2 choice operation
choice = input("Podaj numer działania (1,2,3,4): ")

if __name__ == "__main__":                                   #3 run calculator and result
    if choice in ("1", "3"):
        num1 = float(input ("Podaj liczbę nr 1: "))
        num2 = float(input ("Podaj liczbę nr 2: "))
        print("Podaj następne argumenty lub wciśnij k by zakończyć")               #4 add more arguments
        args = []
        
        while True:
            arg = input("Podaj kolejną liczbę lub k: ")
            if arg == "k":
                break
            args.append(int(arg))
        operations = {
            "add": add,
            "multiply": multiply
        }
        op = input("Co będziemy zrobić? (add, multiply)")
        result = operations[op](num1, num2, *args)
        print(f"Sprawdzam, czy podane wartości są liczbami:", {type(num1)}, {type(num2)}, {type([args])})     #sprawdzam, czy podana wartość jest liczbą
        if choice == '1':
            logging.info(f"Dodaję {num1} i {num2} i {sum(args)}")
            print(f"Dodaję", num1, "i", num2, "i", float(sum(args)))
            print("Wynik dodawania to:", add(num1, num2, sum(args)))
        elif choice == '3':
            logging.info(f"Mnożę {num1} i {num2} i {sum(args)}")
            print(f"Mnożę", num1, "i", num2, "i", float(sum(args)))
            print(f"Wynik mnożenia to:", multiply(num1, num2, sum(args)))
        
    elif choice in ("2", "4"):
        num1 = float(input ("Podaj liczbę nr 1: "))
        num2 = float(input ("Podaj liczbę nr 2: "))
        print(f"Sprawdzam, czy podane wartości są liczbami:", {type(num1)}, {type(num2)})    #sprawdzam, czy podana wartość jest liczbą
        if choice == '2':
            logging.info(f"Odejmuję {num1} i {num2}")
            print(f"Odejmuję", num1, "i", num2)
            print(f"Wynik odejmowania to:", substract(num1, num2))
        elif choice == '4':
            logging.info(f"Dzielę {num1} i {num2}")        
            print(f"Dzielę", num1, "i", num2)
            print(f"Wynik dzielenia to:", (round(divide(num1,num2),2)))
    else : print ("Niepoprawna wartość")

    
