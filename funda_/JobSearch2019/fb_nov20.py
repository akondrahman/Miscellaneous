'''
Akond Rahman 
FB practice
'''

def infixToPostfix(str_par):
    prec = {'*':3, '/':3, '+':2, '-':2, '(':1}
    operandStack = []
    postfixLis = [] 
    str_lis  = str_par.split(' ') 
    for toke in str_lis:
        if ((toke in 'abcdefghijklmnopqrstuvwxyz') or (toke in '0123456789')):
           postfixLis.append(toke)
        elif (toke == '('):
            operandStack.append(toke)
        elif (toke == ')'):
            topToken = operandStack.pop()
            while topToken != '(': 
                postfixLis.append(topToken)
                topToken = operandStack.pop()
        else: 
            while((len(operandStack) > 0) and (prec[operandStack[-1]] >= prec[toke])): 
                postfixLis.append(operandStack.pop())
            operandStack.append(toke)
    while (len(operandStack) > 0):
        postfixLis.append(operandStack.pop())
    return " ".join(postfixLis)

def doMath(op, op1, op2):
    res = 0 
    if op == '*':
        res = op1 * op2 
    elif op == '/':
        res = op1 / op2 
    elif op == '+':
        res = op1 + op2 
    else: 
        res = op1 - op2 
    return res 

def evalPostFix(inp_str):
    tokenList = inp_str.split()
    operandStack = [] 
    for token in tokenList:
        if token in '0123456789': 
            operandStack.append(int(token))
        else: 
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            opera    = token 
            math_res = doMath(opera, operand1, operand2)
            operandStack.append(math_res)
    return operandStack.pop()


if __name__=='__main__':
   infixStr = "( 1 + 7 ) * ( 3 + 6 )"
   postFixStr = infixToPostfix(infixStr)
   print evalPostFix(postFixStr)