from redstat.redload.functions.download import download_data
from redstat.redload.functions.format import format_url, format_file
from redstat.redload.functions.save import save_json


def download_statistic(namespace):
    if namespace.verbose:
        print(namespace)

    resource_name = namespace.name
    resource_url_dict = namespace.url_dict
    resource_type = namespace.type

    url = format_url(resource_url_dict, resource_type, resource_name)
    json_obj = list(download_data(url))

    file = format_file(namespace)
    save_json(json_obj, file)
