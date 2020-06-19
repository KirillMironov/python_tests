import requests as r

url = 'https://www.mvideo.ru/login'

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/75.0.3770.142 Safari/537.36 '

user_data = {'loginCaseSensitive': '', 'login_password': ''}
response = r.post(url, data=user_data)

print(response.text)