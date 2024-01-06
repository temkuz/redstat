from redstat.redload.functions.download import download_statistic
from redstat.redload.functions.save import save_json
from redstat.redload.variables.url import JSON_BASE_URL

from .validate import validate


def download(namespace):

    name = namespace.name
    url = JSON_BASE_URL.format(name)
    statistic = list(download_statistic(url))

    save_json(statistic, namespace.output_file)
