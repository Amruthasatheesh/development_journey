orders={"tea":10,"coffee":24,"dosa":12}
orders_list=[[v,k]for k,v in orders.items()]
print(sorted(orders_list,reverse=True))

languages=["thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]
languages_count={lang:languages.count(lang)for lang in languages}
languages_count_list=[[v,k]for k,v in languages_count.items()]
print(sorted(languages_count_list,reverse=True))