import os


class CalculatorView:
    def get_number(self) -> str:
        self.__clear()
        return input("Digite um número: ")

    def calculator_success(self) -> None:
        # self.__clear()

        message = f'\tCalculo foi concluido com sucesso.'
        print(message)

    def calculator_fail(self) -> None:
        # self.__clear()

        message = f'\tOcorreu um erro ao calcular.'
        print(message)

    def __clear(self):
        os.system('cls||clear')
