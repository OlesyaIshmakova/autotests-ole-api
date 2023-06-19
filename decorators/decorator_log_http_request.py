import logging
import logging.config

import curlify

from config import CURL

logging.config.fileConfig("logging.conf")


def log_http_request(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if CURL:
            logging.info(f"{curlify.to_curl(response.request)}")
        elif response.status_code >= 400:
            logging.info(f"{response.url} {response.status_code}: {response.text}")
        else:
            logging.info(f"{response.url} {response.status_code}")
        return response
    return wrapper
