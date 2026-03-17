print("count of movie records",len(data))
# #3Write a program to read the header row from move.csv and print all column names
# print(list(data[0].keys()))
# #4display all movie titles released in that year from movie.csv
# all_movies_in_a_year={}
# for m in data:
#     year=m.get("Year of Release")
#     name=m.get("Name").split(",")
#     if year in all_movies_in_a_year:
#         all_movies_in_a_year[year]+=name
#     else:
#         all_movies_in_a_year[year]=name
# print(all_movies_in_a_year)

# sorted_lst=[(v,k)for k,v in all_movies_in_a_year.items()]
# print(sorted(sorted_lst,reverse=True))
# #5 print movie with highest rating
# highest=max(di.get("Rating")for di in data)
# highest_rating=[di.get("Name")for di in data if di.get("Rating")==highest]
# print("movie with highest rating",highest_rating)
# #6 print all matching movies from movie.csv
# genre=[di for di in data if di.get("Movie Categories")=="Action"]
# print("Action genre movies",genre)

# #7 
# fw=open("Nested collection\\TASK27\\top_rated.csv","w")
# top_rating=[di.get("Name")for di in data if di.get ("Rating") > "8.0"]
# print(top_rating)
# for data in top_rating:
#     fw.write(data+"\n")
# fw.close()