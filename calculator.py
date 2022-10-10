from calculator_logo import logo

def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b
    
def calculator():
    print(logo)
    should_continue = True
    operation = {"+" : add , "-" : subtract , "*" : multiply , "/" : divide}
    
    operand_a = float(input("Enter the first number :\n"))
    for symbol in operation : print(symbol)
            
    while should_continue:
        operator = input("Enter the symbol :").strip()
        operand_b = float(input("Enter the next number :\n"))
    
        result = operation[operator](operand_a , operand_b)
        print(f"{operand_a} {operator} {operand_b} = {result}")
        if input(f"Type 'y' to continue with {result} or 'n' to start fresh : ").strip().lower() == 'n':
            #should_continue = False
            calculator()
        else:
            operand_a = result

calculator()
