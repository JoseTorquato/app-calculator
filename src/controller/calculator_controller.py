import re


class __CalculatorController:
    def calculator_average(self, number: any) -> any:
        try:
            self.__validator_number(number)

            response = number
            
            return {"success": True, "response": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validator_number(self, number: any) -> any:
        if float(number) or int(number):
            return True
        else:
            raise Exception(f"\tO valor digitado não é um número real.")


calculator_controller = __CalculatorController()
