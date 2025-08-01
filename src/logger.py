import logging
import os
from datetime import datetime

LOG_FILE = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
logs_path = os.path.join(os.getcwd(), 'Logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,

)

if __name__ == '__main__':
    logging.info('Logging has been set up successfully.')
    logging.info(f'Log file created at: {LOG_FILE_PATH}')
    print(f'Log file created at: {LOG_FILE_PATH}')
    # Example log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')