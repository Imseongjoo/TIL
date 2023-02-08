import requests
from pprint import pprint

API_KEY = '7ab85c2ccd889c17aa8c871d33b927e5'

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie' 
    params = { # 
    'api_key' : API_KEY,
    'language': 'ko-KR',
    'region'  : 'KR',
    'query'   : title
    }
    movie_id = 0 # 영화 id
    
    res = requests.get(BASE_URL+path, params=params).json()
    res = res['results']
    
    if res == []:
        return None
    else:
        movie_id = res[0]['id']

    path = f'/movie/{movie_id}/credits' 
    params = { # 
    'api_key' : API_KEY,
    'language': 'ko-KR',
    }
    res = requests.get(BASE_URL+path, params=params).json()
    
    return {'cast': [i['name'] for i in res['cast'] if i['cast_id'] < 10],\
            'crew': [i['name'] for i in res['crew'] if i['department'] == 'Directing']}

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None