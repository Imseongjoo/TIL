import requests
import pprint
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'

while True:
    response = requests.get(URL)
# print(response)
# print(type(response))
# print(dir(response))
    data = response.json()

    print(data.get('data').get('BTC').get('closing_price'))

# 반드시 터미널에서 
# pip install requests
import requests

# https://developers.themoviedb.org/3/movies/get-popular-movies
# https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
# https://api.themoviedb.org/3/movie/2846?api_key=8854669b886a6c07c12ea947bcc2311d

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular' # API 문서에서 적절하게 구성
params = { # 그 문서에서 필요한 params 정의
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'language': 'ko-KR',
    'region': 'KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)
print(response.get('results')[0])

import requests

students = ['gunhee', 'mingi', 'hyunyoung', 'minji', 'yuyoung']

for name in students:
    URL = f'https://api.nationalize.io/?name={name}'
    response = requests.get(URL).json()
    # print(response)
    # print(response.get('country'))
    # print(response.get('country')[0])
    print(name, response.get('country')[0].get('country_id'))