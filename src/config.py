"""Configuration file for the Reddit Summarizer."""

from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, Tuple, TypedDict, TypeVar


class ConfigVars(TypedDict):
    """Type definition for configuration variables."""

    DEFAULT_GPT_MODEL: str
    ATTACH_DEBUGGER: bool
    WAIT_FOR_CLIENT: bool
    DEFAULT_DEBUG_PORT: int
    DEBUGPY_HOST: str
    DEFAULT_CHUNK_TOKEN_LENGTH: int
    DEFAULT_NUMBER_OF_SUMMARIES: int
    DEFAULT_MAX_TOKEN_LENGTH: int
    LOG_FILE_PATH: str
    LOG_COLORS: Dict[str, str]
    REDDIT_URL: str
    LOG_NAME: str
    APP_TITLE: str
    MAX_BODY_TOKEN_SIZE: int
    DEFAULT_QUERY_TEXT: str
    HELP_TEXT: str
    DEFAULT_SYSTEM_ROLE: str


class ConfigLoader:
    """Class for loading configuration variables."""

    CONFIG_VARS: ConfigVars = ConfigVars(
        DEFAULT_GPT_MODEL="gpt-3.5-turbo",
        ATTACH_DEBUGGER=False,
        WAIT_FOR_CLIENT=False,
        DEFAULT_DEBUG_PORT=8765,
        DEBUGPY_HOST="localhost",
        DEFAULT_CHUNK_TOKEN_LENGTH=2000,
        DEFAULT_NUMBER_OF_SUMMARIES=3,  # reduce this to 1 for testing
        DEFAULT_MAX_TOKEN_LENGTH=4096,  # max number of tokens for GPT-3
        LOG_FILE_PATH="./logs/log.log",
        LOG_COLORS={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
        REDDIT_URL="https://www.reddit.com/r/entertainment/comments/1193p9x/daft_punk_announce_new_random_access_memories/",  # noqa: E501 pylint: disable=line-too-long
        LOG_NAME="reddit_gpt_summarizer_log",
        APP_TITLE="Reddit Thread GPT Summarizer",
        MAX_BODY_TOKEN_SIZE=500,
        DEFAULT_QUERY_TEXT=(
            f"(Todays Date: {datetime.now().strftime('%Y-%b-%d')}) Revise and improve"
            " the article by incorporating relevant information from the comments."
            " Ensure the content is clear, engaging, and easy to understand for a"
            " general audience. Avoid technical language, present facts objectively,"
            " and summarize key comments from Reddit. Ensure that the overall"
            " sentiment expressed in the comments is accurately reflected. Optimize"
            " for highly original content. Don't be trolled by joke comments. Ensure"
            " its written professionally, in a way that is appropriate for the"
            " situation. Format the document using markdown and include links from the"
            " original article/reddit thread."
        ),
        DEFAULT_SYSTEM_ROLE="You are a helpful assistant.",
        HELP_TEXT=(
            "#### Help\n"
            "Enter the instructions for the model to follow.\n"
            "It will generate a summary of the Reddit thread.\n"
            "The trick here is to experiment with token lengths and number\n"
            "of summaries. The more summaries you generate, the more likely\n"
            "you are to get a good summary.\n"
            "The more tokens you use, the more likely you are to get a good summary.\n"
            "The more tokens you use, the longer it will take to generate\n"
            "the summary. The more summaries you generate, the more it will cost you.\n"
        ),
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
