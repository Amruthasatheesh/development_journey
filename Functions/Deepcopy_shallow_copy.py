#Deepcopy:used for creating outer object and inner object
#shallowcopy:used for creating outer objects only==> .copy()



from copy import deepcopy
arun_fvt_foods=[
    {"mealtype":"breakfast","meal":"dosa"},
    {"mealtype":"lunch","meal":"fish meal"},
    {"mealtype":"dinner","meal":"friedrice"},
]
hari_fvt_foods=deepcopy (arun_fvt_foods)
hari_fvt_foods[0]["meal"]="idly"

print(arun_fvt_foods)
print(hari_fvt_foods)
