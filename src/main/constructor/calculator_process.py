from numpy import number
from src.controller.calculator_controller import calculator_controller
from src.view.calculator_view import CalculatorView


class CalculatorProcess:
    @staticmethod
    def calculator_process_average() -> any:
        calculator_view = CalculatorView()
        real_number = calculator_view.get_number()

        response = calculator_controller.calculator_average(real_number)

        if response["success"]: calculator_view.calculator_success(response)
        else: calculator_view.calculator_fail()

    @staticmethod
    def calculator_process_std() -> any:
        calculator_view = CalculatorView()
        numbers =  []
        while True:
            numbers.append(calculator_view.get_number())
            other_number = calculator_view.other_number()
            if other_number != "1":
                break

        response = calculator_controller.calculator_std(numbers)

        if response["success"]: calculator_view.calculator_success(response)
        else: calculator_view.calculator_fail()
