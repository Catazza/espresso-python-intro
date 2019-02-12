import logging
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

def logging_basic():

    logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == "__main__":
    logging_basic()