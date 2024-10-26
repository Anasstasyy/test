import json

import requests

apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'y0_AgAAAABTepGiAAysuQAAAAEWCljBAABoKVNpYZ9D1b4HEp5ezbaeIjCQag'}


def createfolder(folder_name):
    params = {'path': folder_name}
    result = requests.put(apiurl, headers=headers, params=params)
    return result.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    result = requests.get(apiurl, headers=headers, params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')