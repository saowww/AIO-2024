import math
def calculate_activation_function(activation_function, x, alpha):
    match activation_function:
        case "sigmoid":
            return calculate_sigmoid(x)
        case "relu":
            return calculate_relu(x)
        case "elu":
            return calculate_elu(x, alpha)
        case _:
            raise Exception(f"{activation_function} is not support")
def calculate_sigmoid(x):
    return 1 / (1+ math.exp(-x))

def calculate_relu(x):
    if x <= 0:
        return 0
    return x

def calculate_relu (x):
    if x<= 0:
        return 0
    return x

def calculate_elu(x, alpha):
    if x<= 0:
        return alpha * (math.exp(x)-1)
    return x

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    
    return True

def exercise2():
    """
    Exercise 2:
    Implement activation functions(sigmoid, relu, elu)
    following user input information
    """
    try: 
        input_x = input("Input x: ")
        if not is_number(input_x):
            raise Exception("x must be a number")
        
        activation_function = input("Input activation function(sigmoi|relu|elu): ")
        x = float(input_x)
        alpha = float(input("Input alpha(default 0.01: )") or "0.01")
        result = calculate_activation_function(activation_function,x,alpha)
        print(f"{activation_function} f({input_x}): {result}")
    except Exception as e:
        print(e)
exercise2()