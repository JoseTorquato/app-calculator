from typing import Type

from flask import request as FlaskRequest
from src.driver.adapter import HTTPRequest
from src.interfaces.calculator_interface import ICalculator


def request_adapter(request: FlaskRequest, process: Type[ICalculator]):
    http_request = HTTPRequest(
        headers=request.headers,
        body=request.json,
        method=request.method,
        url=request.url
    )
    response = process.calculate(http_request.body["input"])
    return response
