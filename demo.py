from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys

logging.info("This is a logging info message from demo.py")


try:
    a = 1 / 0
except Exception as e:
    logging.info("This is an exception message from demo.py")
    raise USVisaException(e, sys)