
"A simple calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. "
"The user is prompted to enter two numbers and a symbol representing the desired operation. "
"The program then performs the calculation and displays the result."
" The user can choose to continue performing calculations or exit the program."



def sum(a, b):
    return a+b

def difference(a, b):
    return a-b

def product(a, b):
    return a*b

def quotient(a, b):
    return a/b

while True:

    a=int(input("FIRST NUMBER:  "))
    sym=input("symbol (+, -, *, /)   ")
    b=int(input("SECOND NUMBER:  "))


    if sym=="+":
        print(sum(a, b))
    elif sym=="-":
        print(difference(a, b))
    elif sym=="*":
        print(product(a, b))
    elif sym=="/":
        print(quotient(a, b))
    else:
        print("invalid symbol")

    cont=input("do you want to continue? (y/n)  ")
    if cont != "y":
        print("Thank you for using the calculator!")
        break
    

