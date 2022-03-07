#!/usr/bin/env python3

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import logging
import sys
import os

logging.basicConfig(level=logging.DEBUG)

auth_token = os.environ["SLACK_BOT_TOKEN"]

client = WebClient(token=auth_token)
# api_response = client.api_test()

if len(sys.argv) > 0:
    msg = " ".join([s.strip() for s in sys.argv[1:]])

try:
    response = client.chat_postMessage(
            channel="C035LSTFM8C", 
            text=msg,
            username="alertbot",
            icon_emoji=":pager:"
    )
except SlackApiError as e:
    assert e.response["error"]


