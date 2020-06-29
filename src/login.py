import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def login():
    login_response = requests.get('http://localhost:8080/captchaImage')
    login_get = login_response.json()
    # login_get = json.loads(login.content)
    img_base64 = login_get['img']
    uuid = login_get['uuid']
    img = base64.b64decode(img_base64)
    with open('a.jpeg', 'wb') as f:
        f.write(img)

    plt.imshow(mpimg.imread('./a.jpeg'))
    plt.show()

    verify_code = input()
    user = 'admin'
    password = 'admin123'
    login_info = {'username': user, 'password': password, 'code': verify_code, 'uuid': uuid}
    login_result = requests.post('http://localhost:8080/login', json=login_info)
    print(login_result.json())
    return login_result.json()['token']


def get_info(token):
    # JWT
    get_info_response = requests.get('http://localhost:8080/getInfo', headers={'authorization': token})
    print(get_info_response.json())


if __name__ == '__main__':
    login()
