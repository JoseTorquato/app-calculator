from src.controller.calculator_controller import calculator_controller
from src.view.calculator_view import CalculatorView


def calculator_process() -> any:
    calculator_view = CalculatorView()
    real_number = calculator_view.get_number()

    response = calculator_controller.calculator_average(real_number)
    print(response)
    if response["success"]: calculator_view.calculator_success()
    else: calculator_view.calculator_fail()
