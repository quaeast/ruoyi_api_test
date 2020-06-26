import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

session = requests.session()

login = session.get('http://localhost:8080/captchaImage')
login_get = login.json()
# login_get = json.loads(login.content)
img_base64 = login_get['img']
uuid = login_get['uuid']
img = base64.b64decode(img_base64)
with open('./a.jpeg', 'wb') as f:
    f.write(img)

plt.imshow(mpimg.imread('./a.jpeg'))
plt.show()

verify_code = input()
user = 'admin'
password = 'admin123'
login_info = {'username': user, 'password': password, 'code': verify_code, 'uuid': uuid}
login_result = session.post('http://localhost:8080/login', json=login_info)


# JWT
get_info = session.get('http://localhost:8080/getInfo', headers={'authorization': login_result.json()['token']})

print(get_info.json())

