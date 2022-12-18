def to_complex(number: dict) -> complex:
    for key, value in number.items():
        comple = complex(key, value)
    return comple
