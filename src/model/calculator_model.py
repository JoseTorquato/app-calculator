from typing import List, Tuple

import numpy as np


class __CalculatorModel:
    def __init__(self) -> None:
        self.__np = np

    def calculator_average(self, number: List) -> any:
        return self.__np.average(number)

    def calculator_std(self, numbers: List) -> any:
        return 1/self.__np.std(numbers)

    def calculator_var(self, numbers: List) -> any:
        return self.__np.var(numbers)
        
calculator_model = __CalculatorModel()
