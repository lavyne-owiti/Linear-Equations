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
    equation = another
    a = len(equation)
    sign = 1
    coefficient = 0
    total = 0
    b = 0
 
      # looping through the  equation
    for j in range(0, a) :
     
        if (equation[j] == '+' or equation[j] == '-' or equation[j] == '*') :  
            if (j > b) :
                total = (total + sign * int(equation[b: j]))
            b = j  
            # print(total) 
        # when we have -x,+x,x
        elif (equation[j] == 'x') :       
            if ((b == j) or
                equation[j - 1] == '+') :
                coefficient += sign
            elif (equation[j - 1] == '-') :
                coefficient = coefficient - sign
            else :
                coefficient = (coefficient + sign * int(equation[b: j]))
                
            b = j + 1   
        # for the equals sign
        elif (equation[j] == '=') :
            if (j > b) :
                total = (total + sign * int(equation[b: j]))
            sign = -1
            b = j + 1   
                
   # for the number left at the end
    if (b < a) :
        total = (total + sign * int(equation[b: len(equation)]))
        
   # endless solution
    if (coefficient == 0 and total == 0) :
        return "Infinite solutions" 
   # when there is no answer
    if (coefficient == 0 and total) :
        return "No solution"
    # x = total sum / coeff of x
    # when you find a - sign it indicates moving numeric value to the right hand side
    ans = -total / coefficient
    return int(ans)
 
equation = "2(4x + 3) + 6 = 24 -4x"
print ("x = {}" .
        format(solve(equation)))
  