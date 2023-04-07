"""Main entry point for the application."""
from .config import ConfigLoader
from .debug_tools import Debugger, DebugOptions
from .log_tools import Logger

app_logger = Logger.get_app_logger()


def print_hello_world() -> None:
    """Print hello world."""
    print("Hello, World!")


def load_config() -> DebugOptions:
    """Load configuration and return an instance of DebugOptions."""
    config = ConfigLoader.get_config()
    return DebugOptions(
        flag=config["ATTACH_DEBUGGER"],
        wait_for_client=config["WAIT_FOR_CLIENT"],
        host=config["DEBUGPY_HOST"],
        port=config["DEFAULT_DEBUG_PORT"],
    )


def main() -> None:
    """Main method."""
    app_logger.info("Loading")

    # Set up the debugger if enabled in the configuration
    debug_options = load_config()
    Debugger.setup_debugpy(app_logger, debug_options)

    print_hello_world()
