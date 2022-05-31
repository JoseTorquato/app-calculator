from flask import Flask, request
from src.main.constructor.calculator_process import CalculatorProcess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo ao calculator'

@app.route('/calculator/averege/', methods=['POST'])
def calculator_averege():
    if request.method == 'POST':
        response = CalculatorProcess.calculator_process_average(request.get_json()["input"])
        return {"request": response}
    else:
        return "Not POST"
