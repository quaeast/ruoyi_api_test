from login import login
import requests


def download(token, filename):
    download_response = requests.get('http://localhost:8080/common/download/resource', headers={'authorization': token})
    return download_response.json()


if __name__ == '__main__':
    print(download(login(), 'a.txt'))
