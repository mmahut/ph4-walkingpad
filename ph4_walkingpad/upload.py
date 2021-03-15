import requests
import logging
import json

logger = logging.getLogger(__name__)


def upload_record(tok, did, cal, timex, dur, distance, step, **kwargs):
    """
    Uploads record to your account
    tok = your JWT token obtained from the app.
    did = device ID, MAC address ff:ff:ff:ff:ff:ff
    """
    url = 'https://eu.app.walkingpad.com/user/api/v2/record'
    cookies = {'user': tok}
    js = {'did': did, 'cal': cal, 'time': timex, 'dur': dur, 'distance': distance, 'step': step,
          'sid': None, 'model': 'A1'}
    logger.info('Upload record: %s' % (json.dumps(js, indent=2)),)
    return requests.post(url, json=js, cookies=cookies, **kwargs)


def get_records(tok, page=1, per_page=10000, timestamp=None, **kwargs):
    url = 'https://eu.app.walkingpad.com/user/api/v2/record?page=%d&per_page=%d' % (page, per_page)
    if timestamp:
        url += '&timestamp=%d' % timestamp
    cookies = {'user': tok}
    return requests.get(url, cookies=cookies, **kwargs)
