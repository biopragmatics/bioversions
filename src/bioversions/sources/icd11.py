URL = "https://icd.who.int/browse/latest-release/mms/en"

import requests


def _get() -> str:
    response = requests.get(URL, allow_redirects=True)
    final_url = response.url
    return final_url[len("https://icd.who.int/browse/"):].split("/")[0]


# https://icd.who.int/browse/latest-release/icf/en