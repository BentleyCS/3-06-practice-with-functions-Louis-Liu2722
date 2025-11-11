#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(n1,n2,n3):
    return (n1+n2+n3)/2
    pass

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(n1,n2,n3,n4):
    return n1*(n1-n2)*(n1-n3)*(n1-n4)
    pass

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(n1,n2,n3):
    s=semiPerimeter(n1,n2,n3)
    area=math.sqrt(s*(s-n1)*(s-n2)*(s-n3))
    return area
    pass


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(n1):
    num=n1*2
    return num
    pass

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(n1,n2):
    num1=n1*-1
    number1=num1+n2
    number2=num1-n2
    return (number1, number2)
    pass
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(n1,n2,n3):
    num1=(n1*n3)*4
    num2=(n2*n2)-num1
    return num2
    pass

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(n1,n2,n3):
    calc=mainCalc(n1,n2,n3)
    sqrt=math.sqrt(calc)
    num1, num2=plusMinus(n2,sqrt)
    deno=denominator(n1)
    root1=num1/deno
    root2=num2/deno
    return (root1, root2)





    pass
