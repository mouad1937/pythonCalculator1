import math


class Calculator:

    def add(self, value1, value2):
        return value1 + value2


    def subtract(self, value1, value2):
         return value1-value2

    def muliply(self, num1 , num2 ):
        return num1*num2

    def devide(self, num1, num2):
        if num2 !=0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed .")

    def square_root(self, num):
        return math.sqrt(num)

    def exponent(self, val1, val2):
        return pow(val1, val2)



