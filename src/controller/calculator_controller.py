import math

from src.model.calculator_model import calculator_model


class __CalculatorController:
    def calculator_average(self, number: any) -> any:
        try:
            number_validator = self.__validator_number(number)
            response = self.__calculator_average(number_validator)

            return {"success": True, "response": "format_response"}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __calculator_average(self, number: any) -> any:
        number_partition = number / 3

        arr_number_partition = [number_partition, number_partition, number_partition]
        
        first_partition = self.__first(arr_number_partition[0])
        second_partition = self.__second(arr_number_partition[1])
        third_partition = arr_number_partition[2]

        return calculator_model.calculator_average([first_partition, second_partition, third_partition])

    def __first(self, n: any) -> any:
        return math.sqrt(((n/4) + 7)) * 0.257

    def __second(self, n: any) -> any:
        return ((n**2.121)/5) + 1

    def __validator_number(self, number: any) -> any:
        if float(number):
            return float(number)
        if int(number):
            return int(number)
        else:
            raise Exception(f"\tO valor digitado não é um número real.")


calculator_controller = __CalculatorController()
