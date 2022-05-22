import os
from email import message
from typing import Dict


class __CalculatorView:
    def get_number(self) -> str:
        self.__clear()
        return input("Digite um número: ")

    def other_number(self) -> str:
        self.__clear()
        message = ''''
                Sim - 1
                Não - Pressione qualquer teclas
            '''
        print(message)
        return input("\tDigite sua opção: ")
    
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


calculator_view = __CalculatorView()
