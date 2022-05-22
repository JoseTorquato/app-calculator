import os
from typing import Dict


class CalculatorView:
    def get_number(self) -> str:
        self.__clear()
        return input("Digite um número: ")
    
    def calculator_success(self, response: Dict) -> None:
        self.__clear()

        message = f'\t{response}'
        print(message)

    def calculator_fail(self) -> None:
        self.__clear()

        message = f'\tOcorreu um erro ao calcular.'
        print(message)

    def __clear(self):
        os.system('cls||clear')
