# class Operation:
#     def __init__(self,operation) :
#         self.equation=["()","^","/","//","%","*","+","-"]
#         alph=string.ascii_letters
#         self.letters=list(alph)
#         self.nums=[0,1,2,3,4,5,6,7,8,9,"."]
       

#     def mathoperation(self,operation):
#        all= self.equation+self.letters+self.nums
#     for math in all:
#             if math not in all:
#                 print("Not supported"+math)

#             elif math[0] in math:
#                 print()
# 7x-2=21

def linearEquation(equation) :
    equation = equation.strip()

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
                print(equation[b: j])
                coefficient = (coefficient + sign * int(equation[b: j]))
                
            b = j + 1   
        # for the equals sign
        elif (equation[j] == '=') :
            if (j > b) :
                total = (total + sign * int(equation[b: j]))
            sign = -1
            b = j + 1   
            # print(total)    
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
 
equation = "7x-2=21"
print ("x = {}" .
        format(linearEquation(equation)))


  # index_of_equals =another.index('=')
    # value_left = another[ :index_of_equals] 
    # value_right = another[index_of_equals+1 :] 
    # print(value_left,value_right) 
    # sign=['=','+','-','*','/']
    # new_index=value_right.index('x')
    # for items in sign:
    #     new_range=sign.index(items)
    #     print(new_range)

    # front_x=value_left[ :new_index +1 ] + value_right[ :new_index+1 ]
    # value_left=front_x 
    # print(front_x)
        
        
    # print(compres_eq)
# print(solve("2x + 45 = 3(x+2)+4") )