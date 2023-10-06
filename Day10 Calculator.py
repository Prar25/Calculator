#Calculator

logo = """
 _____________________
|  _________________  |
| | Pythoncal      0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#add
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#divide
def divide(n1,n2):
    return n1/n2

operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
      }

def calculator():
    print(logo)
    num1=float(input("Please enter the first number: "))
    cont=True
    while cont:
        num2=float(input("Please enter the next number: "))
        for key in operations:
            print(key)
        op_symbol=input("Please choose one operation:")
        func_name=operations[op_symbol]
        res1=func_name(num1,num2)
        print(res1)
        vals=input("To continue the calculation type 'y', to start a new calculation type 'n'. To end the calculator applicatiom type 'e'.\n").lower()
        if vals=="y":
            num1=res1
            cont=True
        elif vals=="n":
            cont=False
            calculator()
        elif vals=="e":
            return

calculator()   
