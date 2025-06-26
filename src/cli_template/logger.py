import logging
import sys

from src.cli_template.settings import settings


def get_logger(name: str, filename: str) -> logging.Logger:
    """Get logger by name."""
    formatter = logging.Formatter(settings.logs_format)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(settings.logs_level)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[stream_handler, file_handler])

    return logging.getLogger(name)


logger = get_logger("cli-template", "cli-template.log")
