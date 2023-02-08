import requests

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '7ab85c2ccd889c17aa8c871d33b927e5', # 키값 입력
        'language': 'ko-KR',
        'region': 'KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    data = response['results']
    return len(data)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20