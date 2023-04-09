"""Logging configuration for the project."""

import logging
import logging.config
import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

from .config import ConfigLoader

T = TypeVar("T")


class Logger:
    """Class to handle logging configuration."""

    config = ConfigLoader
    log_name = config.log_name
    log_file_path = os.path.abspath(config.log_file_path)

    # Create the directory for log files if it doesn't exist
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))
    loggingconfig = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "color": {
                "()": "colorlog.ColoredFormatter",
                "format": "%(log_color)s%(levelname)s:%(message)s",
                "log_colors": config.log_colors,
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "formatter": "color",
                "filename": log_file_path,
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "color",
            },
        },
        "loggers": {
            log_name: {
                "handlers": ["file", "console"],
                "level": logging.INFO,
            }
        },
    }

    # Load the logging configuration using dictConfig
    try:
        logging.config.dictConfig(loggingconfig)
    except ValueError as e:
        print(f"Error occurred during logging configuration: {str(e)}")
        raise

    app_logger = logging.getLogger(log_name)
    app_logger.debug("Logging is configured.")

    @classmethod
    def log(
        cls, func: Callable[..., T], logger: Optional[logging.Logger] = None
    ) -> Callable[..., T]:
        """Decorator to log function calls and return values."""
        if logger is None:
            logger = cls.app_logger

        @wraps(func)  # preserve the metadata of the decorated function.
        def wrapper(*args: Any, **kwargs: Any) -> T:
            logging.info("Calling %s", func.__name__)
            result = func(*args, **kwargs)
            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if logger:
                logger.info("%s: %s returned %s", timestamp, func.__name__, result)
            return result

        return wrapper

    @classmethod
    def get_app_logger(cls) -> logging.Logger:
        """Class method to access the app_logger attribute."""
        return cls.app_logger
