import pytest
from src.controller.calculator_controller import (
    calculator_average_controller, calculator_std_controller,
    calculator_var_controller)


def test_calculator_controler_average_result():
    assert calculator_average_controller.calculate("1")["result"] == 0.6789276387914799
    assert calculator_average_controller.calculate("-1")["result"] == (0.45354416707124456+0.0024063546467115752j)
    assert calculator_average_controller.calculate("12")["result"] == 3.1704416572803424

def test_calculator_controler_average_dict():
    assert calculator_average_controller.calculate("1") == {'calculator': 'average', 'input': 1.0, 'result': 0.6789276387914799, 'success': True}
    assert calculator_average_controller.calculate("-1") == {'success': True, 'calculator': 'average', 'result': (0.45354416707124456+0.0024063546467115752j), 'input': -1.0}
    assert calculator_average_controller.calculate("12") == {'success': True, 'calculator': 'average', 'result': 3.1704416572803424, 'input': 12.0}

def test_exception_calculator_controler_dict():
    assert calculator_average_controller.calculate("a") == {"success": False, "error": "could not convert string to float: 'a'"}
    assert calculator_std_controller.calculate(".") == {"success": False, "error": "could not convert string to float: '.'"}
    assert calculator_var_controller.calculate("-") == {"success": False, "error": "could not convert string to float: '-'"}

def test_calculator_controler_std_result():
    assert calculator_std_controller.calculate(["1", "2", "3"])["result"] == 0.1364596875359298
    assert calculator_std_controller.calculate(["-11", "-2", "33"])["result"] == 0.006362520504658562
    assert calculator_std_controller.calculate(["1.90", "312.234", "10"])["result"] == 0.0009494092013142333

def test_calculator_controler_std_dict():
    assert calculator_std_controller.calculate(["1", "2", "3"]) == {'success': True, 'calculator': 'std', 'result': 0.1364596875359298, 'input': [1.0, 2.0, 3.0]}
    assert calculator_std_controller.calculate(["-11", "-2", "33"]) == {'success': True, 'calculator': 'std', 'result': 0.006362520504658562, 'input': [-11.0, -2.0, 33.0]}
    assert calculator_std_controller.calculate(["1.90", "312.234", "10"]) == {'success': True, 'calculator': 'std', 'result': 0.0009494092013142333, 'input': [1.9, 312.234, 10.0]}


def test_calculator_controler_var_result():
    assert calculator_var_controller.calculate(["1", "2", "3"])["result"] == 0.6666666666666666
    assert calculator_var_controller.calculate(["-11", "-2", "33"])["result"] == 360.2222222222222
    assert calculator_var_controller.calculate(["1.90", "312.234", "10"])["result"] == 20857.576923555553

def test_calculator_controler_var_dict():
    assert calculator_var_controller.calculate(["1", "2", "3"]) == {'success': True, 'calculator': 'var', 'result': 0.6666666666666666, 'input': [1.0, 2.0, 3.0]}
    assert calculator_var_controller.calculate(["-11", "-2", "33"]) == {'success': True, 'calculator': 'var', 'result': 360.2222222222222, 'input': [-11.0, -2.0, 33.0]}
    assert calculator_var_controller.calculate(["1.90", "312.234", "10"]) == {'success': True, 'calculator': 'var', 'result': 20857.576923555553, 'input': [1.9, 312.234, 10.0]}
