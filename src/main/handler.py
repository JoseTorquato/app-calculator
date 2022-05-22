from src.main.constructor.calculator_process import CalculatorProcess
from src.main.constructor.command_process import command_process


def initializer() -> None:
    while True:
        command = command_process()
        if command == "1":
            CalculatorProcess.calculator_process_average()
        elif command == "2":
            CalculatorProcess.calculator_process_std()
        else:
            break
