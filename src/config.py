"""Configuration file for the Reddit Summarizer."""

from functools import wraps
from typing import Any, Callable, Dict, Tuple, TypedDict, TypeVar


class ConfigVars(TypedDict):
    """Type definition for configuration variables."""

    DEFAULT_GPT_MODEL: str
    ATTACH_DEBUGGER: bool
    WAIT_FOR_CLIENT: bool
    DEFAULT_DEBUG_PORT: int
    DEBUGPY_HOST: str
    LOG_FILE_PATH: str
    LOG_COLORS: Dict[str, str]
    LOG_NAME: str


class ConfigLoader:
    """Class for loading configuration variables."""

    CONFIG_VARS: ConfigVars = ConfigVars(
        DEFAULT_GPT_MODEL="gpt-3.5-turbo",
        ATTACH_DEBUGGER=True,
        WAIT_FOR_CLIENT=False,
        DEFAULT_DEBUG_PORT=8765,
        DEBUGPY_HOST="localhost",
        LOG_FILE_PATH="./logs/log.log",
        LOG_COLORS={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
        LOG_NAME="reddit_gpt_summarizer_log",
    )

    @classmethod
    def get_config(cls) -> ConfigVars:
        """Returns a dictionary with configuration parameters."""
        return cls.CONFIG_VARS


R = TypeVar("R")


def with_config(func: Callable[..., R]) -> Callable[..., R]:
    """
    A decorator to inject environment variables into a function.

    Args:
        func (Callable[..., ReturnType]): The function to be decorated.

    Returns:
        Callable[..., ReturnType]: The decorated function with injected environment
        variables.
    """

    @wraps(func)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> R:
        config: ConfigVars = ConfigLoader.get_config()
        return func(*args, config=config, **kwargs)

    return wrapper
