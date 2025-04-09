#def my_function(inp):
#    """This is a docstring"""
#    exp = inp
#    return exp

def my_calculator(first_number, second_number):
    if operatoor == "+":
        return first_number+second_number
    elif operatoor == "-":
        return first_number-second_number
    elif operatoor == "*":
        return first_number*second_number
    elif operatoor == "/":
        return first_number/second_number
    else:
        print("Invalid operator")

temp_val = 0

#always add validaton for inputs. im not doing it here cuz im lazy
while True:
    first_number = float(input("What's the first number?"))
    operatoor = input("Pick an operator:\n+\n-\n*\n/\n")
    second_number = float(input("What's the second number?"))
    print(my_calculator(first_number, second_number))
    if operatoor == "q":
        temp_val = 0
        break
    elif operatoor == "y":
        temp_val = my_calculator(first_number, second_number)
    else:
        break

#cls
#reset all values and start over if they want to
#make it able to keep counting by asking for first number only first time, but always asking for operator.
#very simple but uses dictionaries and loops in functions aswell