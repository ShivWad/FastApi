from fastapi import FastAPI, HTTPException

# Calculate nth Fibonacci


def calculateFibonacci(num):
    if num < 0:
        raise HTTPException(status_code=404, detail="Value of input should not be negative", headers={
                            'ValueError': "Only Positive and 0 are allowed"})  # Handling Exceotion

    first_num = 0
    second_num = 1
    fib = 0
    for i in range(1, num):
        fib = first_num + second_num
        first_num = second_num
        second_num = fib

    return fib

# Calculate Factorial of Given Number


def calculateFactorial(num):
    if num < 0:
        raise HTTPException(status_code=404, detail="Value of input should not be negative", headers={
            'ValueError': "Only Positive and 0 are allowed"})

    if num == 0:
        return 1

    return (num*calculateFactorial(num-1))


app = FastAPI()


@app.get('/')
def index():
    return {'For Factorial': '/factorial', 'For Fibonacci': '/fibonacci'}


@app.get('/factorial/{num}')
def getFactorial(num: int):
    result = calculateFactorial(num)
    return {num: result}


@app.get('/fibonacci/{num}')
def getFibonacci(num: int):
    result = calculateFibonacci(num)
    return {num: result}
