#Following are the criteria for checking the password:
#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12

def str(password):
    SpecialSymbol =['$', '@', '#',] 
    
    if (len(password)<6 or len(password)>12):
        break
    elif not any(char.islower() for char in password):
        break
    elif not any(char.isdigit() for char in password): 
        break
    elif not any(char.isupper() for char in password): 
        break
    elif not any(char in SpecialSymbol for char in password): 
        break
    else:
        return ("Valid Password")