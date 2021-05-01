import logging
import employee

# Create a new logger
logger = logging.getLogger(__name__)
# We'll set the log level to employee logger
logger.setLevel(logging.INFO)

# Now we will add the logging format to the file handler (not logger)
formatter = logging.Formatter('%(levelname)s : %(name)s : %(message)s')
# To specify the employee log file where we want to add our logs to we have to add a file handler
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
# Let's say we want to set the logger level to DEBUG, but we only wanted to log ERRORS to our sample.log file.
# to do that we can set levels to the file_handlers themselves
# So, If you want to set the logger levels to DEBUG but only want to capture ERROR statements and above in specific
# file handler, you got so set file_handler level
file_handler.setLevel(logging.ERROR)

# Now we need to add the file handler to our logger
logger.addHandler(file_handler)


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
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero')
        # Anytime we log an error we can also include the traceback to get more info about what exactly happened
        # logging module allows us to do this very easily
        logger.exception('Tried to divide by zero')
    else:
        return result


num1 = 20
num2 = 0

add_result = add(num1, num2)
logger.info(f'Add: {num1} + {num2} = {add_result}')

sub_result = subtract(num1, num2)
logger.info(f'Sub: {num1} - {num2} = {sub_result}')

mul_result = multiply(num1, num2)
logger.info(f'Mul: {num1} * {num2} = {mul_result}')

div_result = divide(num1, num2)
logger.info(f'Div: {num1} / {num2} = {div_result}')
