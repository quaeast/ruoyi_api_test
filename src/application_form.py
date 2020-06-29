from login import login
import requests


def basic_get(token):
    basic_response = requests.get('http://localhost:8080/student/basic', headers={'authorization': token})
    return basic_response.json()


def basic_post(token):
    content = {'name': 'fangzidong', 'idCardNumber': '210106199812305816'}
    rul = 'http://localhost:8080/student/basic'
    headers = {'authorization': token}
    basic_response = requests.post(rul, headers=headers, json=content)
    return basic_response.json()


if __name__ == '__main__':
    print(basic_post(login()))
