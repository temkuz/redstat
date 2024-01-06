from typing import Any, Generator

from redstat.redload.variables.session import SESSION


def download_statistic(url: str) -> Generator[Any, Any, None]:
    params = {'limit': 100}
    while True:
        response = SESSION.get(url, params=params)
        response.raise_for_status()
        json_response = response.json().get('data')

        for child in json_response.get('children'):
            yield child.get('data')

        after = json_response.get('after')
        if after is None:
            break
        params['after'] = after
