#!/usr/bin/env python3 

from pdpyras import APISession
from pprint import pprint
import logging
import os

logging.basicConfig(level=logging.DEBUG)

auth_token = os.environ["PAGERDUTY_BOT_TOKEN"]

client = APISession(auth_token)

user = client.rget('/users/PKPQYO7')

pprint(user)
