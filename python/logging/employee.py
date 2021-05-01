import logging

# Create a new logger
logger = logging.getLogger(__name__)
# We'll set the log level to employee logger
logger.setLevel(logging.INFO)

# Now we will add the logging format to the file handler (not logger)
formatter = logging.Formatter('%(levelname)s : %(name)s : %(message)s')
# To specify the employee log file where we want to add our logs to we have to add a file handler
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

# Now we need to add the file handler to our logger
logger.addHandler(file_handler)


class Employee:
    """A sample employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(f'Created Employee {self.fullname} - {self.email}')

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'


emp1 = Employee('John', 'Smith')
emp2 = Employee('Corey', 'Schafer')
emp3 = Employee('Jane', 'Doe')
