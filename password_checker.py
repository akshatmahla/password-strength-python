def lengthCheck(password):
    if len(password) >= 8:  #check password length greater than equal to 8
        return True
    else:
        return False

def Uppercase(password):
    for i in range(len(password)):
        if password[i].isupper():       #if any uppercase letter found, return true
            return True
    return False                        #return false otherwise

def Lowercase(password):
    for i in range(len(password)):
        if password[i].islower():      #if any lowercase letter found, return true
            return True
    return False                        #return false othewise
def DigitCheck(password):
    for i in range(len(password)):
        if password[i] >= '0' and password[i] <= '9':   #if any digit is found return true
            return True
    return False                #return false otherwise
def SymbolCheck(password):
    for i in range(len(password)):
        if Uppercase(password[i]) is False and Lowercase(password[i]) is False and DigitCheck(password[i]) is False:        #return true if it is symbol
            return True
    print("Password does not contain a symbol")
    return False


flag = False
while not flag:
    flag = True
    strength = 0
    password = input("Enter Password : ")
    if not SymbolCheck(password):
      flag = False
    else :
        strength += 1

    if not lengthCheck(password):
      flag = False
      print("Password not at least 8 characters long")
    else :
        strength += 1

    if not DigitCheck(password):
      flag = False
      print("Password does not contain a digit")
    else :
        strength += 1

    if not Lowercase(password):
        flag = False
        print("Password does not contain lowercase letter")
    else :
        strength += 1

    if not Uppercase(password):
       flag = False
       print("Password does not must contain uppercase letter")
    else :
        strength += 1
    if flag:
        print("-->>Very strong password<<--")
        break
    else:
        if strength == 1:
            print("-->>Very Weak Password<<--")
        elif strength== 2:
            print("-->>Weak Password<<--")
        elif strength == 3:
            print("-->>Good password<<--")
        elif strength == 4:
            print("-->>Strong password<<--")