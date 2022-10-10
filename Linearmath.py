
def solve(eq):
    # eq=input(str("enter an equation:"))
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
        
        print(f"Step 1:Identify the bracketed part: \n{stringToReplace}") 
        for char in equationInsideBrackets:
            if char == "x":
                newString = newString + "x"
            elif char == "=" or char == "*" or char=="+" or char=="-" or char=="/":
                newString = newString + char
            else:
                stri = int(multiplier) * int(char)
                newString = newString + str(stri)
                print(f"Step 2:Workout inside the bracket:\n {newString}")
        another = another.join(compres_eq.replace(stringToReplace, newString))
        print(f"Step 3:Show the equation without the bracket:\n {another}")
    #   move the stuff on the right side to the left side
    else:
        another = eq
    equation = another
    length_equation = len(equation)
    sign = 1
    coefficient_of_x = 0
    total = 0
    intercept = 0
    for items in range(0, length_equation) :
     
        if (equation[items] == '+' or equation[items] == '-' or equation[items] == '*') :  
            if (items > intercept) :
                total = (total + sign * int(equation[intercept: items]))
            intercept = items 
        elif (equation[items] == 'x') :       
            if ((intercept == items) or
                equation[items - 1] == '+') :
                coefficient_of_x += sign
            elif (equation[items - 1] == '-') :
                coefficient_of_x = coefficient_of_x - sign
            else :
                coefficient_of_x = (coefficient_of_x + sign * int(equation[intercept: items]))        
            intercept = items + 1  
       
        elif (equation[items] == '=') :
            if (items > intercept) :
                total = (total + sign * int(equation[intercept: items]))
            sign = -1
            intercept = items + 1          
  
    if (intercept < length_equation) :
        total = (total + sign * int(equation[intercept: len(equation)]))
        print(f"Step 4:divide both side with the coefficient: \n{coefficient_of_x}x = {total}")

    if (coefficient_of_x == 0 and total == 0) :
        return "Infinite solutions" 

    if (coefficient_of_x == 0 and total) :
        return "No solution"

    ans = -total / coefficient_of_x
    print(ans)
    return int(ans)

equation=" 7x-2=21 "  
print ("x = {}" .
        format(solve(equation)))
  