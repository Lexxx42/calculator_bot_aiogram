from calculator_bot_aiogram.calc.operations import *


def send_to_controller(number1, function, number2):
    match function:
        case '+':
            answer = str(sum_value(float(number1), float(number2)))
            return answer
        case '-':
            answer = str(sub_value(float(number1), float(number2)))
            return answer
        case 'pow':
            answer = str(pow_usual(float(number1), float(number2)))
            return answer
        case '*':
            answer = str(mult(float(number1), float(number2)))
            return answer
        case '/':
            answer = str(div_usual(float(number1), float(number2)))
            return answer
        case '//':
            answer = str(div_integer(float(number1), float(number2)))
            return answer
        case '%':
            answer = str(div_modul(float(number1), float(number2)))
            return answer
        case '_':
            return ''
