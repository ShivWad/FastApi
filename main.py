from numpy.lib.shape_base import dsplit
from modules import math_module, string_module
import streamlit as st


# Using streamlit to create a easy to use GUI
# Step 1 --> Select Module
# Step 2 --> Select Function
# Step 3 --> Enter input
# Step 4 --> Get results


st.title('FastApi Module Calling')
st.markdown('Select a **Module**.')

option = st.selectbox("", ('Math Module', 'String Module'))

st.write('You selected :', option)

if option == 'Math Module':
    math_option = st.selectbox(
        "Select a function to call:", ('Calculate Factorial', 'Calculate Nth Fibonacci'))
    if math_option == 'Calculate Factorial':
        input_num = st.number_input('Enter a number: ', step=1)
        result = math_module.getFactorial(input_num)
        st.success('Factorial of {}  is {}'.format(
            input_num, result[input_num]))

    else:
        input_num = st.number_input('Enter a number: ', step=1)
        complexity = st.selectbox('Select time complexity:', ('1', 'n'))
        result = math_module.getFibonacci(input_num, complexity=complexity)
        st.success('{}th fibonacci number is {} , we used O({})'.format(
            input_num, result[input_num], complexity))

else:
    string_option = st.selectbox(
        'Select a function to call:', ('Generate String', 'Calculate Legth'))
    if string_option == 'Generate String':
        input_char = st.text_input('Enter a character')
        length = st.number_input('Enter a number: ', step=1, min_value=1)
        result = string_module.getRandomString(input_char, length)
        st.success('Random string of character {} is {}'.format(input_char, result[input_char][length]))
        
    else:
        input_string = st.text_input('Enter a character')
        result = string_module.calcLengh(input_string=input_string)
        st.success('Length of {} is {}'.format(input_string, result[input_string]))