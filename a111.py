import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(a, b):
    logging.debug(f'Starting divide function with a={a}, b={b}')
    try:
        result = a / b
        logging.debug(f'Division successful: result={result}')
        return result
    except ZeroDivisionError:
        logging.error('Error: Division by zero')
        return None

# Example usage
x = 10
y = 0

logging.info('Program started')
logging.debug(f'Values before division: x={x}, y={y}')

result = divide(x, y)

logging.debug(f'Result after division: {result}')
logging.info('Program ended')
