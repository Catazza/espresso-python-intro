from src.logexception.exceptionhandler import *
# Error & Exception handling
import logging
import inspect
from src.logexception.logframework import LoggerInitialiser
import src.logexception.module_logger as ml


logger = logging.getLogger(__name__)
LoggerInitialiser(conf_method='yaml', conf_path='./config/log_config.yaml')


class ErrorInput(enumerate):
    ZERODIV = 1
    STRTYPE = 2
    OTHER = 3


@exception_handler((FileNotFoundError, TypeError, ZeroDivisionError, ApplicationException), logger, silence=True)
def parse_csv_and_get_columns(filename, error_req=None):
    csv_file = None
    logger.info('Reading CSV file')
    with open(filename, 'r') as csv_file:
        lines = csv_file.readlines()
        for line in lines[1:]:
            val = line.split(",")
            if error_req == ErrorInput.STRTYPE:
                test_str_div = val[0] / val[11]
            elif error_req == ErrorInput.ZERODIV:
                test_zero_div = int(val[0]) / int(val[11])
            elif error_req == ErrorInput.OTHER:
                raise ApplicationException(val)


if __name__ == "__main__":
    logger.info('STARTING PROGRAM-----')
    ml.alive_again()
    parse_csv_and_get_columns(filename="data/test.csv")
    parse_csv_and_get_columns(filename="../../data/flights.csv", error_req=ErrorInput.STRTYPE)
    parse_csv_and_get_columns(filename="../../data/flights.csv", error_req=ErrorInput.ZERODIV)
    parse_csv_and_get_columns(filename="../../data/flights.csv", error_req=ErrorInput.OTHER)
