a = False

while a == False:
    a = int(input("Select an integer for the dividend"))
    b = int(input("Select another integer for the divisor"))
    c = a % b
    if c == 0:
        print(a, "is divisable by", b)
    else:
        print(a, "is not divisable by", b)

    a = False