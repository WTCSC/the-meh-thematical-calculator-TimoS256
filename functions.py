def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return 'divide_by_zero_error'
    return a / b
def exp(a, b):
    if a < 0:
        return 'imaginary_result_error'
    return a ** b