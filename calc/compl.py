def to_complex(number: dict) -> complex:
    for key, value in number.items():
        complex_number = complex(key, value)
        return complex_number
