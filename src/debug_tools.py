"""Debugging tools."""
# debugger.py
import logging
from dataclasses import dataclass

import debugpy  # type: ignore


@dataclass
class DebugOptions:
    """Class to hold debug options."""

    flag: bool = False
    wait_for_client: bool = False
    host: str = "localhost"
    port: int = 8765


class Debugger:
    """Class to handle debugging tools."""

    _debugger_set_up = False

    @classmethod
    def setup_debugpy(
        cls,
        logger: logging.Logger,
        options: DebugOptions,
    ) -> None:
        """
        Set the debug flag and start the debugpy server.

        :param logger: Logger instance to log messages.
        :param flag: Debug flag to enable/disable debugging.
        :param wait_for_client: Flag to wait for the debug client to attach.
        :param host: Host for the debugpy server.
        :param port: Port for the debugpy server.
        """
        if options.flag:
            cls._activate_debugging(logger, options)
        else:
            cls._deactivate_debugging(logger)

    @classmethod
    def _activate_debugging(
        cls,
        logger: logging.Logger,
        options: DebugOptions,
    ) -> None:
        if not cls._debugger_set_up and not debugpy.is_client_connected():
            try:
                debugpy.listen((options.host, options.port))
                cls._debugger_set_up = True

                if options.wait_for_client:
                    logger.info("Waiting for debug client attach...")
                    debugpy.wait_for_client()
                    logger.info("...attached!")

                logger.info(
                    f"Remote debugging activated (host={options.host},"
                    f" port={options.port})"
                )

            except (ConnectionError, ValueError, TypeError) as error:
                logger.exception(f"Debugger setup failed with error: {error}")

    @classmethod
    def _deactivate_debugging(cls, logger: logging.Logger) -> None:
        if cls._debugger_set_up:
            logger.info("Remote debugging is NOT active")
            cls._debugger_set_up = False
            logger.info("Remote debugging is NOT active")
            cls._debugger_set_up = False
