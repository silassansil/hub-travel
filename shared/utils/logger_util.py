import logging


def logger(_name):
    # create logger
    logger_instance = logging.getLogger(_name)
    logger_instance.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger_instance.addHandler(ch)
    return logger_instance
