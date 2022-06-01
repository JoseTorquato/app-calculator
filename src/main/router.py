from flask import Flask, request
from src.controller.calculator_controller import (
    calculator_average_controller, calculator_std_controller,
    calculator_var_controller)
from src.main.handler import request_adapter

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo ao calculator'

@app.route('/calculator/averege/', methods=['POST'])
def calculator_averege():
    if request.method == 'POST':
        response = request_adapter(request, calculator_average_controller)
        return {"response": response}

@app.route('/calculator/std/', methods=['POST'])
def calculator_std():
    if request.method == 'POST':
        response = request_adapter(request, calculator_std_controller)
        return {"response": response}

@app.route('/calculator/var/', methods=['POST'])
def calculator_var():
    if request.method == 'POST':
        response = request_adapter(request, calculator_var_controller)
        return {"response": response}
