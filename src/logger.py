import logging


# create a logger
logger = logging.getLogger("global_logger")
# set logger level, debug level will handle all levels of debug including
# DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.DEBUG) 

# allow logs printed onto the console
console_controller = logging.StreamHandler()
console_controller.setLevel(logging.DEBUG)

# save logs to file
from main import LOGGER_LOCATION
file_handler = logging.FileHandler(LOGGER_LOCATION)
file_handler.setLevel(logging.DEBUG)

# restrain logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_controller.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_controller)
