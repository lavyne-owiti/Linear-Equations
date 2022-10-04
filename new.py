equation = "2x + 45 = 3(x+2)+4"
def solve(eq):
    compres_eq = eq.replace(" ", "")
    index_of_first_bracket = None
    index_of_last_bracket = None
    try:
        index_of_first_bracket = compres_eq.index("(")
        index_of_last_bracket = compres_eq.index(")")
    except:
        print('result')
    # remove the brackets 
    another=""
    if(index_of_first_bracket is not None and index_of_first_bracket > 0):
        multiplier = compres_eq[index_of_first_bracket - 1]
        equationInsideBrackets = compres_eq[index_of_first_bracket + 1 : index_of_last_bracket]
        newString = ""
        stringToReplace = compres_eq[index_of_first_bracket - 1 : index_of_last_bracket+1]
        
        print(stringToReplace)
    
        for char in equationInsideBrackets:
            print(char)
            if char == "x":
                newString = newString + multiplier + "x"
            elif char == "=" or char == "*" or char=="+" or char=="-" or char=="/":
                newString = newString + char
            else:
                stri = int(multiplier) * int(char)
                newString = newString + str(stri)
        another = another.join(compres_eq.replace(stringToReplace, newString))
        print(another)
    #   move the stuff on the right side to the left side
    else:
        another = eq
    index_of_equals =another.index('=')
    value_left = another[ :index_of_equals] 
    value_right = another[index_of_equals+1 :] 
    print(value_left,value_right) 
    new_index=value_left.index('x')
    new_index=value_right.index('x')
    front_x=value_left[ :new_index ] 
    fron_x=value_right[ :new_index ]
    print(front_x,fron_x)
        
        
    # print(compres_eq)
print(solve("2 + 3 + 2x + 45 = 3(x+2)+4") )