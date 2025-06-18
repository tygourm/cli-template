import logging

from src.cli_template.core.settings import settings

formatter = logging.Formatter(settings.logs_format)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(settings.logs_level)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(settings.logs_filename)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


def get_logger(name: str) -> logging.Logger:
    """Get logger by name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers = [stream_handler, file_handler]
    return logger
