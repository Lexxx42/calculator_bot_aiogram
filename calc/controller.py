from .operations import *
from ..loader import logging

ERROR_MESSAGE = "Input data is incorrect"


def send_to_controller(number1, function, number2):
    match function:
        case '+':
            try:
                answer = str(sum_value(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '-':
            try:
                answer = str(sub_value(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case 'pow':
            try:
                answer = str(pow_usual(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '*':
            try:
                answer = str(mult(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '/':
            try:
                answer = str(div_usual(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '//':
            try:
                answer = str(div_integer(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '%':
            try:
                answer = str(div_modul(float(number1), float(number2)))
            except ValueError:
                answer = ERROR_MESSAGE
                logging.info(ERROR_MESSAGE)
            return answer
        case '_':
            return ''
