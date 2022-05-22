import math
import re
from typing import Dict, List

from numpy import number
from src.model.calculator_model import calculator_model


class __CalculatorController:
    def calculator_average(self, number: any) -> Dict:
        try:
            number_validator = self.__validator_number(number)

            response = self.__build_average(number_validator)

            return {"success": True, "calculator": "average", "result": response, "input": number_validator}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
            
    def calculator_std(self, numbers: List) -> Dict:
        try:
            arr_numbers = [self.__validator_number(n) for n in numbers]

            response = self.__build_std(arr_numbers)

            return {"success": True, "calculator": "std", "result": response, "input": arr_numbers}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
            
    def calculator_var(self, numbers: List) -> Dict:
        try:
            arr_numbers = [self.__validator_number(n) for n in numbers]

            response, result = self.__build_var(arr_numbers)
            
            return {"success": response, "calculator": "var", "result": result, "input": arr_numbers}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __build_average(self, number: any) -> any:
        number_partition = number / 3

        arr_number_partition = [number_partition, number_partition, number_partition]
        
        first_partition = self.__first(arr_number_partition[0])
        second_partition = self.__second(arr_number_partition[1])
        third_partition = arr_number_partition[2]

        return calculator_model.calculator_average([first_partition, second_partition, third_partition])

    def __build_std(self, numbers: List) -> any:
        multiplicate_numbers = list(map(lambda n: n * 11, numbers))
        pow_numbers = list(map(lambda n: n ** 0.95, multiplicate_numbers))

        return calculator_model.calculator_std(pow_numbers)

    def __build_var(self, numbers: List) -> any:
        calculator_std = self.__build_std(numbers)
        calculator_var = calculator_model.calculator_var(numbers)

        return calculator_var > calculator_std, calculator_var

    def __first(self, n: any) -> any:
        return math.sqrt(((n/4) + 7)) * 0.257

    def __second(self, n: any) -> any:
        return ((n**2.121)/5) + 1

    def __validator_number(self, number: any) -> any:
        if float(number):
            return float(number)
        else:
            raise Exception(f"\tO valor digitado não é um número real.")


calculator_controller = __CalculatorController()
