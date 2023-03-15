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

# import json

# # 아래 코드 수정 금지
# movie_json = open('data/movie.json', encoding='UTF8')
# movie = json.load(movie_json)

# genres_json = open('data/genres.json', encoding='UTF8')
# genres_list = json.load(genres_json)

# # 이하 문제 해결을 위한 코드 작성
# genre_names = []
# genre_ids = movie['genre_ids']
# for genre_id in genre_ids:
#     for genre_dict in genres_list:
#         if genre_id == genre_dict['id']:
#             genre_names.append(genre_dict['name'])

# new = {
#     'id': movie['id'],
#     'title': movie['title'],
#     'vote_average': movie['vote_average'],
#     'overview': movie['overview'],
#     'genre_names': genre_names,
# }
# print(new)
