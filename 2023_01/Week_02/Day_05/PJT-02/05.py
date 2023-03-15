import requests
from pprint import pprint

API_KEY = '7ab85c2ccd889c17aa8c871d33b927e5'


def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.

    # 영화 id 찾기
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'query': title
    }
    movie_id = 0  # 영화 id

    res = requests.get(BASE_URL+path, params=params).json()
    res = res['results']

    if res == []:
        return None
    else:
        movie_id = res[0]['id']

    # 추천영화 찾기!
    path = f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR',
    }
    res = requests.get(BASE_URL+path, params=params).json()
    res = res['results']

    return [i['title'] for i in res]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
