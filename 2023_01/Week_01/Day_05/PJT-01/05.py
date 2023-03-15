import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
key_list = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
movie_info_dict = {}
for key in key_list:
    movie_info_dict[key] = movie[key]
print(movie_info_dict)

# import json

# # 아래 코드 수정 금지
# movie_json = open('data/movie.json', encoding='UTF8')
# movie = json.load(movie_json)

# # 이하 문제 해결을 위한 코드 작성
# new_movie = {
#     'id': movie['id'],
#     'title': movie['title'],
#     'vote_average': movie['vote_average'],
#     'overview': movie['overview'],
#     'genre_ids': movie['genre_ids'],
# }
# print(new_movie)
