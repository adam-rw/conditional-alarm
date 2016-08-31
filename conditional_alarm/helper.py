import os
import logging
from time import strftime, localtime
import sys


class Helper(object):
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    def logger(msg, lvl):
        timestamp = strftime("%D %H:%M:%S", localtime())
        msg = '{}: {}'.format(timestamp, msg)
        lvl = lvl.upper()
        log_file = 'log.txt'
        log_level = 'debug'
        logging.basicConfig(filename=log_file, level=log_level.upper())

        if lvl == 'DEBUG':
            logging.debug(msg)
        else:
            logging.info(msg)
