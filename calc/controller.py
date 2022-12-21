import datetime
import uuid
from logg import logging
import user_interface
import model_div
import model_mult
import model_pow
import model_sub
import model_sum
import compl
import model_div_options


def session() -> tuple:
    session_id = uuid.uuid1()
    session_datetime = datetime.datetime.now()
    operation_result = start()
    finish(operation_result[2])
    return session_id, session_datetime, operation_result


def start() -> tuple:
    user_interface.main_menu()
    number_type = user_interface.numb_type
    interface_data = user_interface.t
    number1 = interface_data[0]
    number2 = interface_data[1]
    operation = interface_data[2]
    logging.info(f'num1 = {number1}, num2 = {number2}, operation_code = {operation}')
    match number_type:
        case 1:
            logging.info('Operation with real numbers.')
            result = operations(number1, number2, operation)
        case 2:
            logging.info('Operation with complex numbers.')
            compl1 = compl.to_complex(number1)
            compl2 = compl.to_complex(number2)
            result = operations(compl1, compl2, operation)
        case _:
            print('числа не заданы, завершаем программу без вычислений')
            result = 'отсутствует'
    logging.info(f'{result} result of operation')
    return number_type, interface_data, result


# работает с комплексными, если не указывать явно тип данных
def operations(a, b, o: int) -> str:
    match o:
        case 1:
            res = str(model_sum.sum_value(a, b))
        case 2:
            res = str(model_sub.sub(a, b))
        case 3:
            res = str(model_mult.mult(a, b))
        case 4:
            res = str(model_div.div_complex_number(a, b))
        case 41:
            res = str(model_div.div_rational_number(a, b))
        case 42:
            res = str(model_div_options.div_integer(a, b))
        case 43:
            res = str(model_div_options.div_modul(a, b))
        case 5 | 6:
            res = str(model_pow.pow_new(a, b))
        case _:
            res = 'error'
    return res


def finish(r: str) -> None:
    user_interface.view_result(r)
