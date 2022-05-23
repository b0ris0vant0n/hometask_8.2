import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file_path: str, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = { 'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path" : disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        requests.put(href, data=open(filename, 'rb'))

if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    uploader.upload('/netology/my.txt', 'myfile.txt')