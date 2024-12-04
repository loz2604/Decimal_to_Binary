number = 0.1
binary = [0,0,0,0,0,0,0,0]

def value_check():
    global number
    while int(number) == False or number > 255 or number < 0:
        try:
            number = int(input("Please enter a number between 0 and 255 >>> "))
            if number > 255 or number < 0:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
            try:
                number = int(input("Please enter a number between 0 and 255 >>> "))
                print(number)
            except ValueError:
                print("Invalid input")

value_check()

decimal = number

def check():
    global number
    decimal = number
    if decimal >= 128:
        num128check()
    elif decimal >= 64:
        num64check()
    elif decimal >= 32:
        num32check()
    elif decimal >= 16:
        num16check()
    elif decimal >= 8:
        num8check()
    elif decimal >= 4:
        num4check()
    elif decimal >= 2:
        num2check()
    elif decimal >= 1:
        num1check()
    elif decimal == 0:
        print(number, " converted into binary is >>> ", *binary, sep="")

def num128check():
    global decimal
    binary[0] = 1
    decimal -= 128
    end_check()

def num64check():
    global decimal
    binary[1] = 1
    decimal -= 64
    end_check()
    
def num32check():
    global decimal
    binary[2] = 1
    decimal -= 32
    end_check()

def num16check():
    global decimal
    binary[3] = 1
    decimal -= 16
    end_check()

def num8check():
    global decimal
    binary[4] = 1
    decimal -= 8
    end_check()

def num4check():
    global decimal
    binary[5] = 1
    decimal -= 4
    end_check()

def num2check():
    global decimal
    binary[6] = 1
    decimal -= 2
    end_check()
def num1check():
    global decimal
    binary[7] = 1
    decimal -= 1
    end_check()

def end_check():
    if decimal == 0:
        print(number, " converted into binary is >>> ", *binary, sep="")
    else:
        if decimal >= 64:
            num64check()
        elif decimal >= 32:
            num32check()
        elif decimal >= 16:
            num16check()
        elif decimal >= 8:
            num8check()
        elif decimal >= 4:
            num4check()
        elif decimal >= 2:
            num2check()
        elif decimal >= 1:
            num1check()
check()