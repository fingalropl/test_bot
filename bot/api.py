import json
import requests

BASE_URL = 'http://127.0.0.1:8000/api'
def registrate(username):
    response=requests.post(f'{BASE_URL}/user/', json={"username":f"{username}"})
    print(response)

def check_token(username):
    response = requests.get(f'{BASE_URL}/user/token_check/?search={username}')
    k = response.json()
    if not k:
        print('Мимо, такого пользователя нет')
    else:
        token = k[0].get('token')
        return token

def edit_token(username, m):
    response = requests.put(f'{BASE_URL}/user/token_edit/', json={"username":f"{username}","m":f"{m}"})

def search_task(text):
    response = (requests.get(f'{BASE_URL}/task_list/?search={text}')).json()
    if not response:
        return 1
    else:
        # print(response)
        task=[]
        for dicionary in response:
            task.append(dicionary['text'])
        return task

def search_answer(text):
    response = (requests.get(f'{BASE_URL}/task_list/?search={text}')).json()
    if not response:
        return 'Похожих вопросов не найдено'
    else:
        answer = (response[0])['answer']
        res = [text, answer]
        return res