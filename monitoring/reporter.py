import json
from typing import Dict

import requests
from retrying import retry

from monitoring import config
from monitoring.lib.utils import retry_if_5xx_or_connection_error


class Reporter:
    def __init__(self):
        self._api_url = config.REPORT_HOST_ENDPOINT
        self._headers = {
            "Authorization": config.CLIENT_TOKEN
        }

    def report_latency(self, payload: Dict) -> None:
        url_suffix = '01e7t9yby45168yw0t7ewtcfst'
        self._make_request(method='post', url_suffix=url_suffix, body=payload)

    def report_speed(self, payload: Dict) -> None:
        url_suffix = '01e7tac210v87w8t7p1732z9tm'
        self._make_request(method='post', url_suffix=url_suffix, body=payload)

    @retry(
        retry_on_exception=retry_if_5xx_or_connection_error,
        stop_max_attempt_number=5,
        wait_fixed=5000
    )
    def _make_request(self, method: str, url_suffix: str, body=None) -> requests.Response:
        if method == 'get':
            response = requests.get(
                '{}/{}'.format(self._api_url, url_suffix),
                headers=self._headers
            )
        elif method == 'post':
            response = requests.post(
                '{}/{}'.format(self._api_url, url_suffix),
                data=json.dumps(body),
                headers=self._headers
            )
        elif method == 'put':
            response = requests.put(
                '{}/{}'.format(self._api_url, url_suffix),
                data=json.dumps(body),
                headers=self._headers
            )
        else:
            raise ValueError(f'method `{method}` not implemented')

        response.raise_for_status()
        return response
