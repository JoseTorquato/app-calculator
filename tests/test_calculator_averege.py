import pytest
from src.controller.calculator_controller import calculator_controller


def test_calculator_controler_average_result():
    assert calculator_controller.calculator_average("1")["result"] == 0.6789276387914799
    assert calculator_controller.calculator_average("-1")["result"] == (0.45354416707124456+0.0024063546467115752j)
    assert calculator_controller.calculator_average("12")["result"] == 3.1704416572803424

def test_calculator_controler_average_dict():
    assert calculator_controller.calculator_average("1") == {'calculator': 'average', 'input': 1.0, 'result': 0.6789276387914799, 'success': True}
    assert calculator_controller.calculator_average("-1") == {'success': True, 'calculator': 'average', 'result': (0.45354416707124456+0.0024063546467115752j), 'input': -1.0}
    assert calculator_controller.calculator_average("12") == {'success': True, 'calculator': 'average', 'result': 3.1704416572803424, 'input': 12.0}
