# FastApi
FastApi app, deployed on streamlit

##Use python 3.6.13

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements


```bash
pip install -r requirements.txt
```

## Usage

In your terminal run 

```python
 streamlit run main.py

```
for GUI interface

## For using swagger UI of FastApi 
Go to modules directory run 
for Math_module
```
 uvicorn math_module:app  --reload 
```
for string_module
```
 uvicorn string_module:app  --reload    
```
for swagger UI, go to 
```
http://127.0.0.1:8000/docs
```
