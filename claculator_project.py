def add(n1, n2):
    return n1 + n2 
#TODO: Write out the other 3 functions - substract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 



#TODO: Add these 4 function into a dictionary as the values. Keys = "+", "-", "*", "/"

operation = {

"+": add,
"-": subtract,
"*": multiply,
"/": divide,

}


#TODO: Use the dictionary operations to perform the calculations.
# print(operation["*"](9 , 4))

def calculator():
    should_continue = True 

    num1 = float(input("What's the first number?:"))

    while should_continue:

        for symbol in operation:
            print(symbol)

        operation_symbol = (input("Pick an operation"))

        num2 = float(input("What's the next number?:"))

        result = (operation[operation_symbol](num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {result}")

        
        user_input = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")
        if user_input == "y":
            num1 = result 
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
        
calculator()
    

