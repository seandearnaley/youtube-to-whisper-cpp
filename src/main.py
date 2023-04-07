# Configuration and utilities


# Configuration and utilities
from .config import ConfigLoader, ConfigVars


def init() -> None:
    # Initialize the application
    # This is where you would load the configuration, connect to the database, etc.
    print("Initializing the application...")


def main(config: ConfigVars) -> None:
    print("Hello, World!")


if __name__ == "__main__":
    # Load the configuration and start the application
    _config = ConfigLoader.get_config()
    main(_config)
