from urllib.parse import urlencode
import requests

APP_ID = 6775582
AUTH_URL = 'https://oauth.vk.com/authorize?'

# client_id=5490057&display=page&&scope=friends&response_type=token&v=5.52

auth_data = {
    'client_id' : APP_ID,
    'display' : 'page',
    'redirect_uri' : 'https://oauth.vk.com/blank.html',
    'response_type' : 'token',
    'scope' : 'status,video,friends',
    'v' : '5.92'
}

# print(AUTH_URL + (urlencode(auth_data)))
my_token = '0af64ab407a8cf7f4718334f754450899424cc5273e0191c334840799c2f6feea881eb0b366c34e3bb4f7'
new_id = 54900572
new_id_2 = 347655652

def get_friends(id, token):
    params = {
        'access_token': token,
        'v': '5.92',
        'user_id': id,
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()


def get_mutual_friends(id_1, id_2, token):
    params = {
        'access_token': token,
        'v': '5.92',
        'source_uid': id_1,
        'target_uid': id_2
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    return response.json()

# artyom = User(token)
# status = artyom.set_status('лалал')
# print(status)

# print(get_friends(new_id, my_token))
print(get_mutual_friends(new_id, new_id_2, my_token))
