from fastapi import FastAPI, HTTPException
import math


# Calculate nth Fibonacci with O(n) complexity
def calculateFibonacciOn(num):
    if num < 0:
        raise HTTPException(status_code=404, detail="Value of input should not be negative", headers={
                            'ValueError': "Only Positive and 0 are allowed"})  # Handling Exception

    first_num = 0
    second_num = 1
    fib = 0
    for i in range(1, num):
        fib = first_num + second_num
        first_num = second_num
        second_num = fib

    return fib

# Calculate nth Fibonacci with O(1) complexity


def calculateFibonaccioO1(num):
    if num < 0:
        raise HTTPException(status_code=404, detail="Value of input should not be negative",
                            headers={'ValueError': "Only Positive and 0 are allowed"})  # Handling Exception
    phi = (1 + math.sqrt(5)) / 2
    fibo = round(pow(phi, num)/math.sqrt(5))
    return fibo
# Calculate Factorial of Given Number


def calculateFactorial(num):
    if num < 0:
        raise HTTPException(status_code=404, detail="Value of input should not be negative",
                            headers={'ValueError': "Only Positive and 0 are allowed"})

    if num == 0:
        return 1

    return (num*calculateFactorial(num-1))


app = FastAPI()


@app.get('/')
def index():
    return {'For Factorial': '/factorial', 'For Fibonacci': '/fibonacci'}


@app.get('/factorial/{num}')
def getFactorial(num: int):
    """
    Calculating Factorial: Arguments ---> int
    Calculating Facotorial of given number using recursion Time Complexity: O(n)
    """
    result = calculateFactorial(num)
    return {num: result}


@app.get('/fibonacci/{num}')
def getFibonacci(num: int, complexity):
    """
    Calculating Fibonacci: Arguments ---> int, complexity = 1 or n \n
    Calculating fibonacci of given number by given time complexity
    """
    if complexity == 'n':
        result = calculateFibonacciOn(num)
    elif complexity == '1':
        result = calculateFibonaccioO1(num)
    else:
        raise HTTPException(status_code=404, detail='Choose time complexity between O(1) or O(n)', headers={
            'ComplexityError': 'input either 1 or n'})
    return {num: result}
