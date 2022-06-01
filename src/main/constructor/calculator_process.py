from re import U
from typing import Type

from src.controller.calculator_controller import (
    calculator_average_controller, calculator_std_controller,
    calculator_var_controller)
from src.view.calculator_view import calculator_view


class CalculatorProcess:
    @staticmethod
    def calculator_process_average(real_number) -> any:
        return CalculatorProcess.__calculator_response(calculator_average_controller.calculate(real_number))

    @staticmethod
    def calculator_process_std() -> any:
        numbers = CalculatorProcess.__input_numbers()
        CalculatorProcess.__calculator_response(calculator_std_controller.calculate(numbers))

    @staticmethod
    def calculator_process_var() -> any:
        numbers = CalculatorProcess.__input_numbers()
        CalculatorProcess.__calculator_response(calculator_var_controller.calculate(numbers))

    @staticmethod
    def __input_numbers():
        numbers =  []
        while True:
            numbers.append(calculator_view.get_number())
            other_number = calculator_view.other_number()
            if other_number != "1":
                break
        
        return numbers

    @staticmethod
    def __calculator_response(response):
        if response["success"]: return calculator_view.calculator_success(response)
        else: return calculator_view.calculator_fail()
