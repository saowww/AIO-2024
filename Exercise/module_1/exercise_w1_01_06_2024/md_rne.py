def calculate_md_rne(y, y_hat, n, p):
    try:
        if not isinstance(y, (int, float))or not isinstance(y_hat, (int, float)):
            raise ValueError("y and y_hat must be a number")
        
        if not isinstance(n,int) or not isinstance(p,int):
            raise ValueError("n and p must be an interger")
        print(((y ** (1/n)) - (y_hat ** (1/n))) ** p)
    except Exception as e:
        print(e)
calculate_md_rne(100, 49.5, 2, 1)