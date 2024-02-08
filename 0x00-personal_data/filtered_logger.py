#!/usr/bin/env python3
"""Filter file"""
from typing import List
import re
import logging
import os
from os import environ


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """Function that returns the log message obfuscated"""
    for field in fields:
        message = re.sub(
            f'{field}=[^{separator}]+',
            f'{field}={redaction}', message)
    return message
