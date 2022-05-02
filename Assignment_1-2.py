#!/usr/bin/env python


def Solver(id):
    '''
    Solve the inequality: -x^2 + b*x - 5000 > 0
    
    Paramater
    ---------
    ID : int, Student ID number.
    
    Return
    ------
    Values : list, All the solutions satisfy the inequality.
    '''
    Equation = lambda x, b: b * x - x ** 2 - 5000

    b = (id + 100) * 2 

    Values = []

    for x in range(3000):
        if Equation(x, b) > 0:
            Values.append(x)
    
    print(len(Values))
    return Values
    

if __name__ == '__main__':
    My_id = 52
    Values = Solver(My_id)