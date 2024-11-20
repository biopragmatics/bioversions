"""Utilities for interacting with Slack."""

import logging
from functools import lru_cache

import pystow
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

__all__ = [
    "post",
]

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def _get_client(token: str | None = None) -> WebClient | None:
    token = pystow.get_config("bioversions", "slack_api_token", passthrough=token)
    if token is None:
        return None
    return WebClient(token=token)


def post(text: str, channel: str = "random", token: str | None = None):
    """Post the message to a given Slack channel."""
    client = _get_client(token)
    if client is None:
        return None

    if not channel.startswith("#"):
        channel = f"#{channel}"
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text,
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        if not e.response["ok"]:
            raise ValueError('Response is not "ok"') from e
        logger.warning(f"Got an error: {e.response['error']}")
    else:
        return response


if __name__ == "__main__":
    post("Slack test!")
