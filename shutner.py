from stack import *
def toPostfix(infix):
    return infix
def evaluate(expression):
    a = Stack()
    operators = {'*','/','+','-'}
    for i in range(0,len(expression)):
        if expression[i] in operators:
            num1 = a.pop()
            num2 = a.pop()
            if expression[i] == '*':
                a.push(num1*num2)
            elif expression[i] == '/':
                a.push(num2/num1)
            elif expression[i] == '+':
                a.push(num1+num2)
            else:
                a.push(num2-num1)
        else:
            a.push(int(expression[i]))
    return a.pop()
