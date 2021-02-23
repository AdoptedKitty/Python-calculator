user = False

while user == False:
    user = int(input(
    """Calculator menu:
    1- Addition calculator
    2- Subtraction calculator
    3- Multiplication calculator
    4- Division calculator
    5- Divisibility calculator
    6- Odd or even calculator
    7- Exponent calculator
    """))
    if user == 1:
        a = int(input("Select your first addend"))
        b = int(input("Select your second addend"))
        print(a + b)
    if user == 2:
        c = int(input("Select the number you're subtracting"))
        d = int(input("Select the number you're subtracting by"))
        print(c - d)
    if user == 3:
        e = int(input("Select your factor"))
        f = int(input("Select another factor"))
        print(e * f) 
    if user == 4:
        g = int(input("Select your dividend"))
        h = int(input("Select your divisor"))
        print(g * h)
    if user == 5:
        i = int(input("Select your dividend"))
        j = int(input("Select your divisor"))
        k = i % j
        if c == 0:
            print(i, "is divisable by", j)
        else:
            print(i, "is not divisable by", j)
    if user == 6:
        l = int(input("Select an integer"))
        m = l % 2
        if m == 0:
            print(l, "is even")
        else:
            print(l, "is odd")
    if user == 7:
        n = int(input("Select an integer"))
        o = int(input("Enter the exponent"))
        print(n ** o)

        
    user = False
