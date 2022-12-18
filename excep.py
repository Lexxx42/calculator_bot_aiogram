""" This file is for data validation. Developed by Alexander Konukhov. """
import logging

MUST_BE_INTEGER = 'Incorrect input! Input must be an integer'
MUST_BE_A_REAL = 'Incorrect input! Input must be a real number'
DIVISION_BY_ZERO = "Division by zero!"


def validation_mode() -> int:
    """ Function for check user's input for calculator's mode. """
    while True:
        try:
            calc_mode = int(input("Enter the calculator's mode: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if calc_mode in [0, 1, 2]:
            if calc_mode == 0:
                logging.info('Finished work from main menu')
            else:
                logging.info(f'main mode of calculator = {calc_mode}')
            return calc_mode
        print("Incorrect input! Please look at the available modes.")
        logging.exception("Incorrect input! Please look at the available modes.")


def validation_operation(data_type) -> int:
    """ Function for check user's input for operation. """
    while True:
        try:
            operation_type = int(input("Enter operation code: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if operation_type in range(7) and data_type == 1:
            logging.info(f'operation code = {operation_type}')
            return operation_type
        elif operation_type in range(6) and data_type == 2:
            logging.info(f'operation code = {operation_type}')
            return operation_type
        print("Incorrect input! Please look at the available operation codes.")
        logging.exception("Incorrect input! Please look at the available operation codes.")


def validation_rational_input(main_operation) -> tuple[float, float]:
    """ Function for check user's input for rational numbers. """
    output_numbers = []
    while len(output_numbers) < 2:
        try:
            number = float(input(f"Enter number{len(output_numbers) + 1}: "))
        except ValueError:
            print(MUST_BE_A_REAL)
            logging.exception(MUST_BE_A_REAL)
            continue
        if main_operation == 4 and len(output_numbers) == 1 and number == 0:
            print(DIVISION_BY_ZERO)
            logging.exception(DIVISION_BY_ZERO)
            continue
        output_numbers.append(number)
        if main_operation == 6:
            output_numbers.append(0.5)
    logging.info(f'num1 = {output_numbers[0]}, num2 = {output_numbers[1]}')
    return output_numbers[0], output_numbers[1]


def validation_complex_input(main_operation) -> tuple[dict[float, float], dict[float, float]]:
    """ Function for check user's input for complex numbers. """
    output_complex = []
    number_input = 1
    while len(output_complex) < 4 and main_operation != 5 or len(output_complex) < 2 and main_operation == 5:
        try:
            if len(output_complex) % 2 == 0:
                number = float(input(f"Enter {number_input} real part: "))
            else:
                number = float(
                    input(f"Enter {number_input} imaginary number: "))
                number_input += 1
        except ValueError:
            print(MUST_BE_A_REAL)
            logging.exception(MUST_BE_A_REAL)
            continue
        if main_operation == 4 and len(output_complex) == 3 and output_complex[2] == 0 and number == 0:
            number_input -= 1
            print(DIVISION_BY_ZERO)
            logging.exception(DIVISION_BY_ZERO)
            continue
        output_complex.append(number)
    power = -1
    if main_operation == 5:
        while power < 0:
            try:
                power = float(input("Enter real power value: "))
            except ValueError:
                print(MUST_BE_A_REAL)
                logging.exception(MUST_BE_A_REAL)
                continue
            if power < 0:
                print("Number must be greater or equal than zero.")
                logging.exception("Number must be greater or equal than zero.")
                continue
            first_imaginary_number = {}
            first_imaginary_number[output_complex[0]] = output_complex[1]
            second_imaginary_number = {}
            second_imaginary_number[power] = 0
            return first_imaginary_number, second_imaginary_number
    first_imaginary_number = {}
    second_imaginary_number = {}
    first_imaginary_number[output_complex[0]] = output_complex[1]
    second_imaginary_number[output_complex[2]] = output_complex[3]
    logging.info(f'num_complex1 = {first_imaginary_number}, num_complex2 = {second_imaginary_number}')
    return first_imaginary_number, second_imaginary_number


def validation_additional_operation() -> int:
    """ Function for check user's input for additional operation. """
    while True:
        try:
            add_operation_code = int(
                input("Enter additional operation code: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if add_operation_code in range(4):
            logging.info(f'additional operation code = {add_operation_code}')
            return add_operation_code
        print("Incorrect input! Please look at the available additional operation codes.")
        logging.exception("Incorrect input! Please look at the available additional operation codes.")
