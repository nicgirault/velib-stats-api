"""To communicate with the velib API."""
import requests
import json

import config
import logging


def get_stations_data():
    response = requests.get(
        config.VELIB_API_URL + '/stations?apiKey=%s' % (config.VELIB_API_KEY)
    )

    if response.status_code != 200:
        logging.error('Failed to fetch stations data')
        logging.error(response.text)
    else:
        return json.loads(response.text)
