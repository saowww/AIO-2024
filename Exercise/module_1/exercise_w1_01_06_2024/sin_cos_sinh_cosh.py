import math

def validateInput(x,n):
    if not isinstance(x, (int,float)):
        raise ValueError("x must be a number")

    if not isinstance(n, int):
        raise ValueError("n must be an interger")

    if n < 0:
        raise ValueError("n must be a positive interger")

    return float(x), int(n)

def approx_sin(x,n):
    try:
        x, n = validateInput(x, n)
        sin_x = 0
        for i in range(n):
            sin_x += (-1)**i * (x**(2 *i +1)) / math.factorial(2 * i + 1)
        print(round(sin_x,4))
    except Exception as e:
        print(e)
def approx_cos(x,n):
    try:
        x, n = validateInput(x,n)
        cos_x = 0
        for i in range(n):
            cos_x += (-1)**i*(x**(2*i))/ math.factorial(2*i)
        print(round(cos_x,2))
    except Exception as e:
        print(e)
        
def approx_sinh(x,n):
    try:
        x, n = validateInput(x, n)
        sinh_x = 0
        for i in range(n):
            sinh_x += x ** (2*i + 1) / math.factorial(2*i +1)
        print(round(sinh_x,2))
    except Exception as e:
        print(e)

def approx_cosh(x, n):
    try:
        x,n = validateInput(x, n)
        cosh_x = 0
        for i in range(n):
            cosh_x += x**(2*i)/math.factorial(2*i)
    
        print(round(cosh_x,2))
    except Exception as e:
        print(e)

approx_sin(3.14,10)
approx_cos(3.14,10)
approx_sinh(3.14,10)
approx_cosh(3.14,10)