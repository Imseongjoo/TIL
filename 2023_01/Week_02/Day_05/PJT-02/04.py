import requests
from pprint import pprint


def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '7ab85c2ccd889c17aa8c871d33b927e5',  # 키값 입력
        'language': 'ko-KR',
        'region': 'KR',
        'query': title
    }

    response = requests.get(BASE_URL+path, params=params).json()
    res = response['results']
    for n in res:
        if title in n['title']:
            return n['id']
        else:
            return None

    # movie_dict = requests.get(BASE_URL+path, params=params).json().get('results', None)

    # if movie_dict == None:
    #     return None
    # search_movies = [movie.get('title') for movie in movie_dict]
    # return search_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
