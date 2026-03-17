movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]
#display all movie title
# all_movie_title=[lst[1]for lst in movies]
# print(all_movie_title)
# #display movie with top rating
# top_rating=max([lst[4]for lst in movies])
# print(top_rating)
# top_rting_movie=[lst[1]for lst in movies if lst[4]==top_rating]
# print(top_rting_movie)
#display kannada movies
#display movies where actoir is yash
#which language has most number of movies all language=["k",""]
#movie with mxm budget
#languages
# kannada_movies=[lst[1] for lst in movies if lst[3]=="Kannada"]
# print(kannada_movies)
# actor_yash_movies=[lst[1] for lst in movies if lst[2]=="Yash"]
# print(actor_yash_movies)
#which language has most number of movies all language
kannada_language=[m[3]for m in movies]
kannada_language_count={k:kannada_language.count(k)for k in kannada_language}
language_list=[[v,k]for k,v in kannada_language_count.items()]
print(sorted(language_list,reverse=True))#o/p:[[3, 'Kannada'], [2, 'Telugu'], [1, 'Malayalam']]
#movies with mxm budget
# mxm_budget_movies=max([lst[5]for lst in movies])
# mxm_budget_movies_name=[lst[1]for lst in movies if lst[5]==mxm_budget_movies]


# print(mxm_budget_movies)
# print(mxm_budget_movies_name)
# languages=[lst[3]for lst in movies]
# print(languages)
