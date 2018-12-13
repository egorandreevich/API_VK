import requests
from pprint import pprint

class User:
    def __init__(self, i):
        self.user_id_number = i
        self.friends_dic = self.get_friends()
        self.friends_set = set(self.friends_dic['response']['items'])

    def get_friends(self):
        params = {
            'access_token': self.my_token,
            'v': '5.92',
            'user_id': self.user_id_number,
            'count' : '500'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()

    def make_class_items(self):
        list_1 = user1 & user2
        list_2 = []
        print(list_1)
        for user in list_1:
            # print(user)
            user = User(user)
            list_2.append(user)
        return list_2

    def __and__(self, other):
        friends_list = list(self.friends_set & other.friends_set)
        friends_list_as_users = []
        print('Уже ищу... подожди 10 секунд')
        for user in friends_list:
            user = User(user)
            friends_list_as_users.append(user)
        return friends_list_as_users

    def __str__(self):
        return 'https://vk.com/id'+str(self.user_id_number)

    my_token = 'dbd6ac2f8fc162e0cbeac3a76f364520645f28053451b586bcaba74a232a3d02bdcc1b811da9dbf6efdf7'
    user_id_number = 0
    new_list = list()


user1 = User(171691064) #Для примера взял страницу Евгения
user2 = User(7858) #И первого попавшегося его друга

print(user1 & user2)
print(user1)
