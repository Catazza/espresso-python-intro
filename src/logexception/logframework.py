'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''

import logging
import json
import yaml
import functools
from logging.config import fileConfig


class LoggerInitialiser:
    """
    Class to initialise a logger instance. Supports json, yaml and ini config files.
    """
    def __init__(self, conf_method=None, conf_path=None, default_level=logging.INFO):
        self.config_handlers = {
            'yaml': LoggerInitialiser.setup_logging_yaml,
            'json': LoggerInitialiser.setup_logging_json,
            'ini':  LoggerInitialiser.setup_logging_ini
        }
        self._setup_logging(conf_method=conf_method, conf_path=conf_path, default_level=default_level)

    @staticmethod
    def setup_logging_json(conf_path):
        """
        Set-up logging configuration from a json file.
        :param conf_path: path to config file.
        :return: None - sets-up logger
        """
        with open(conf_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)

    @staticmethod
    def setup_logging_yaml(conf_path):
        """
        COMING SOON
        Set-up logging configuration from a yaml file.
        :param conf_path: path to config file.
        :return: None - sets-up logger
        """
        with open(conf_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    @staticmethod
    def setup_logging_ini(conf_path):
        """
        COMING SOON
        Set-up logging configuration from a ini file.
        :param conf_path: path to config file.
        :return: None - sets-up logger
        """
        raise NotImplementedError

    def _setup_logging(self, conf_method, conf_path, default_level):
        """
        Method to set-up the logger config according to the methodology preferred. supports JSON, INI and YAML.

        :param conf_method: string deciding which configuration to fire up. One of 'yaml', 'json', 'ini'.
        :param conf_path: path to the configuration file
        :param default_level: if no config method is provided, what level to initialise the logger at.
        :return:
        """
        if conf_method is None:
            logging.basicConfig(level=default_level)
        else:
            if conf_path is None:
                raise ValueError('Must provide a config file path for config method {}'.format(conf_method))
            self.config_handlers[conf_method](conf_path)


def func_exec_logger(logger):
    """
    Simple decorator to signal start and end of a function execution. Used to avoid clogging the code over and over
    with the beginning and end of logging.

    :param logger: the logger object to fire up logs. Passed as parameter to allow flexibility in handlers/formatters.
    :return: the decorated function
    """
    def logger_wrapper(func):
        @functools.wraps(func)
        def logger_func(*args, **kwargs):
            logger.info('Started execution of {}().'.format(func.__name__))
            result = func(*args, **kwargs)
            logger.info('Execution terminated of {}()'.format(func.__name__))
            return result
        return logger_func
    return logger_wrapper


if __name__ == "__main__":
    LoggerInitialiser(conf_method='json', conf_path='./config/log_config.json')
