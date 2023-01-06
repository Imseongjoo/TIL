import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
movies = {}
for key in key_list:
    movies[key] = movies_list[key]
    print(movies)

