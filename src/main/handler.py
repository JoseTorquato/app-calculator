from src.main.constructor.calculator_process import calculator_process
from src.main.constructor.command_process import command_process


def initializer() -> None:
    while True:
        command = command_process()
        if command == "1":
            calculator_process()
