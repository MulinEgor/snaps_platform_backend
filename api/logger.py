import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler = logging.FileHandler('logs/api.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
