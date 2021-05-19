import string
import random
from fastapi import FastAPI, HTTPException

# Generating Random string of n length and 
def generateRandom(input_Char, n):
    if len(input_Char) > 1:
        raise HTTPException(status_code=404, detail="length of input should be equal to 1", headers={
                            'ValueError': "Only Characters are allowed"})
    if n < 1:
        raise HTTPException(status_code=404, detail="Value of length should be greater than 0", headers={
            'ValueError': "Only Positive are allowed (n>0)"})
    randString = ''.join(random.choices(
        string.ascii_letters + string.digits, k=n-1))
    resulted_string = input_Char+randString

    return resulted_string


app = FastAPI()


@app.get('/')
def index():
    return {'For RandomNumber': '/genrateString/{input_Char}/{n}', 'For Calculate Length': '/calculatelength/{input_string}'}


@app.get('/calculatelength/{input_string}')
def calcLengh(input_string):
    return {input_string: len(input_string)}


@app.get('/genrateString/{input_Char}/{n}')
def getRandomString(input_Char, n: int):
    generatedString = generateRandom(input_Char=input_Char, n=n)
    return {input_Char: {n: generatedString}}
