from art import logo

print(logo)

# calculated
def add(n1,n2):
    return n1+n2

# minus
def minus(n1,n2):
    return n1-n2

# multiply
def multi(n1,n2):
    return n1*n2

# divided
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : minus,
    "*" : multi,
    "/" : divide
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for operated in operations:
        print(operated)
    
    end_calculated = False
    while not end_calculated:
        operated_sysmbol = input("Pick an operation from the line above: ")
        
        num2 = float(input("What's the next number?: "))  
        calculated_function = operations[operated_sysmbol]
        
        answer = calculated_function(num1,num2)
        
        print(f"{num1} {operated_sysmbol} {num2} = {answer}")      
        if input(f"Type 'y' to continue with {answer} or 'n' to Stat new Calculated: ") == "y":
            num1 = answer
        else:
            end_calculated = True
            calculator()

calculator()