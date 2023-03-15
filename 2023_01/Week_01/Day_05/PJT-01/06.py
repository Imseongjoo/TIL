import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
key_list = ['id', 'title', 'poster_path',
            'vote_average', 'overview', 'genre_ids']
movies = {}
for key in key_list:
    movies[key] = movies_list[key]
    print(movies)

# import json

# # 아래 코드 수정 금지
# movies_json = open('data/movies.json', encoding='UTF8')
# movies_list = json.load(movies_json)

# genres_json = open('data/genres.json', encoding='UTF8')
# genres_list = json.load(genres_json)

# # 이하 문제 해결을 위한 코드 작성
# new_movie_list = []

# for movie in movies_list:
#     new_movie = {
#         'id': movie['id'],
#         'title': movie['title'],
#         'poster_path': movie['poster_path'],
#         'vote_average': movie['vote_average'],
#         'overview': movie['overview'],
#         'genre_ids': movie['genre_ids'],
#     }
#     new_movie_list.append(new_movie)

# print(new_movie_list)
