import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
key_list = ['id', 'title', 'vote_average', 'overview', 'genre_names']
movie_info_dict = {}
for key in key_list:
    movie_info_dict[key] = movie[key]
print(movie_info_dict)