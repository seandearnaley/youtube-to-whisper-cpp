"""Module for loading configuration variables."""
from functools import wraps
from typing import Any, Callable


class ConfigLoader:
    """Class for loading configuration variables."""

    attach_debugger: bool = True
    wait_for_client: bool = False
    default_debug_port: int = 8765
    debugpy_host: str = "localhost"
    log_file_path: str = "./logs/log.log"
    log_colors: dict[str, str] = {
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
    log_name: str = "logs/log.txt"


def with_config(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to inject environment variables into a function.

    Args:
        func (Callable[..., ReturnType]): The function to be decorated.

    Returns:
        Callable[..., ReturnType]: The decorated function with injected environment
        variables.
    """

    @wraps(func)
    def wrapper(*args: tuple[Any, ...], **kwargs: dict[str, Any]) -> Any:
        config: ConfigLoader = ConfigLoader()
        return func(*args, config=config, **kwargs)

    return wrapper
