from typing import List, Tuple

import numpy as np


class __CalculatorModel:
    def __init__(self) -> None:
        self.__np = np

    def calculator_average(self, number: List) -> Tuple:
        return self.__np.average(number)

    def calculator_std(self):
        return self.__np.std()
        
calculator_model = __CalculatorModel()
