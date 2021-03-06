import math
from typing import Dict, List

from src.driver.calculator_model import calculator_model
from src.interfaces.calculator_interface import ICalculator
from src.utils.validator_number import validator_number


class __CalculatorAveregeController(ICalculator):
    def calculate(self, number: any) -> Dict:
        try:
            number_validator = validator_number(number)

            response = self.__build_average(number_validator)

            return {"success": True, "calculator": "average", "result": response, "input": number_validator}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __build_average(self, number: any) -> any:
        number_partition = number / 3        
        first_partition = self.__first(number_partition)
        second_partition = self.__second(number_partition)
        third_partition = number_partition

        return calculator_model.calculator_average([first_partition, second_partition, third_partition])

    def __first(self, n: any) -> any:
        return math.sqrt(((n/4) + 7)) * 0.257

    def __second(self, n: any) -> any:
        return ((n**2.121)/5) + 1

calculator_average_controller = __CalculatorAveregeController()

class __CalculatorStdController(ICalculator):
    def calculate(self, numbers: List) -> Dict:
        try:
            arr_numbers = [validator_number(n) for n in numbers]

            response = self.__build_std(arr_numbers)

            return {"success": True, "calculator": "std", "result": response, "input": arr_numbers}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __build_std(self, numbers: List) -> any:
        multiplicate_numbers = list(map(lambda n: n * 11, numbers))
        pow_numbers = list(map(lambda n: n ** 0.95, multiplicate_numbers))

        return calculator_model.calculator_std(pow_numbers)

calculator_std_controller = __CalculatorStdController()

class __CalculatorVarController(ICalculator):
    def calculate(self, numbers: List) -> Dict:
        try:
            arr_numbers = [validator_number(n) for n in numbers]
            result = self.__build_var(arr_numbers)
            
            return {"success": True, "calculator": "var", "result": result, "input": arr_numbers}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __build_var(self, numbers: List) -> any:
        calculator_std = calculator_std_controller.calculate(numbers)["result"]
        calculator_var = calculator_model.calculator_var(numbers)
        if calculator_var > calculator_std:
            return calculator_var
        else:
            raise Exception(f"O valor m??dio {calculator_var}, nao ?? maior que o desvio padrao {calculator_std}")

calculator_var_controller = __CalculatorVarController()
