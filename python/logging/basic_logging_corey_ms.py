import logging
import employee

logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s : %(levelname)s : %(message)s')


def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    return x / y


num1 = 20
num2 = 10

add_result = add(num1, num2)
logging.info(f'Add: {num1} + {num2} = {add_result}')

sub_result = subtract(num1, num2)
logging.info(f'Sub: {num1} - {num2} = {sub_result}')

mul_result = multiply(num1, num2)
logging.info(f'Mul: {num1} * {num2} = {mul_result}')

div_result = divide(num1, num2)
logging.info(f'Div: {num1} / {num2} = {div_result}')
