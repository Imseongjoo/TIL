import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 

# import json

# # 아래 코드 수정 금지
# movie_json = open('data/movie.json', encoding='UTF8')
# movie = json.load(movie_json)

# genres_json = open('data/genres.json', encoding='UTF8')
# genres_list = json.load(genres_json)

# # 이하 문제 해결을 위한 코드 작성
# genre_ids = movie['genre_ids']

# genre_list = []
# for genre_id in genre_ids:
#     for genre_dict in genres_list:
#         if genre_id == genre_dict['id']:
#             genre_list.append(genre_dict['name'])

# print(genre_list)