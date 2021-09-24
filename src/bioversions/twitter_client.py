# -*- coding: utf-8 -*-

"""Utilities for interacting with Twitter."""

from functools import lru_cache
from typing import Optional

import pystow
import tweepy


@lru_cache(maxsize=1)
def _get_api(
    consumer_key: Optional[str] = None,
    consumer_secret: Optional[str] = None,
    access_token: Optional[str] = None,
    access_token_secret: Optional[str] = None,
) -> Optional[tweepy.API]:
    consumer_key = pystow.get_config("bioversions", "consumer_key", passthrough=consumer_key)
    consumer_secret = pystow.get_config(
        "bioversions", "consumer_secret", passthrough=consumer_secret
    )
    access_token = pystow.get_config("bioversions", "access_token", passthrough=access_token)
    access_token_secret = pystow.get_config(
        "bioversions", "access_token_secret", passthrough=access_token_secret
    )

    if consumer_key and consumer_secret and access_token and access_token_secret:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Create API object
        api = tweepy.API(auth)
        return api

    return None


def post(text: str):
    """Post the message to Twitter."""
    api = _get_api()
    if api is None:
        return None
    return api.update_status(text)


if __name__ == "__main__":
    post("Twitter test!")
