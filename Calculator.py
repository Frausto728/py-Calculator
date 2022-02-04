for i in range(3):
    operator = input("Choose an operator +,-,/,*: ")


    try:
        number_1 = int(input("enter a number: "))
        number_2 = int(input("enter another: "))

    except:
        raise NameError("Invalid Number")

    def addition (number_1,number_2) : 
        total = number_1 + number_2
        return total

    def subtraction(number_1,number_2):
        total = number_1 - number_2
        return total

    def multi(number_1,number_2):
        total = number_1 * number_2
        return total

    def div(number_1,number_2):
        total = number_1 / number_2
        return total
    
    if operator == "+":
        print("The answer is", addition(number_1,number_2))
    
    elif operator == "-":
        print("The answer is", subtraction(number_1,number_2)) 

    elif operator == "*":
        print("The answer is", multi(number_1,number_2)) 

    elif operator == "/":
        print("The answer is", div(number_1,number_2)) 

    else:
        print("Invalid Operator")

#Comment Test   


