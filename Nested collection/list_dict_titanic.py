titanic_data = [
    {"id": 1, "survived": 0, "pclass": 3, "class": "Third", "name": "Braund, Mr. Owen Harris", "sex": "male", "age": 22, "fare": 7.25},
    {"id": 2, "survived": 1, "pclass": 1, "class": "First", "name": "Cumings, Mrs. John Bradley (Florence)", "sex": "female", "age": 38, "fare": 71.28},
    {"id": 3, "survived": 1, "pclass": 3, "class": "Third", "name": "Heikkinen, Miss. Laina", "sex": "female", "age": 26, "fare": 7.92},
    {"id": 4, "survived": 1, "pclass": 1, "class": "First", "name": "Futrelle, Mrs. Jacques Heath (Lily)", "sex": "female", "age": 35, "fare": 53.10},
    {"id": 5, "survived": 0, "pclass": 3, "class": "Third", "name": "Allen, Mr. William Henry", "sex": "male", "age": 35, "fare": 8.05},
    {"id": 6, "survived": 0, "pclass": 3, "class": "Third", "name": "Moran, Mr. James", "sex": "male", "age": None, "fare": 8.45},
    {"id": 7, "survived": 0, "pclass": 1, "class": "First", "name": "McCarthy, Mr. Timothy J", "sex": "male", "age": 54, "fare": 51.86},
    {"id": 8, "survived": 0, "pclass": 3, "class": "Third", "name": "Palsson, Master. Gosta Leonard", "sex": "male", "age": 2, "fare": 21.07},
    {"id": 9, "survived": 1, "pclass": 3, "class": "Third", "name": "Johnson, Mrs. Oscar W (Elisabeth)", "sex": "female", "age": 27, "fare": 11.13},
    {"id": 10, "survived": 1, "pclass": 2, "class": "Second", "name": "Nasser, Mrs. Nicholas (Adele)", "sex": "female", "age": 14, "fare": 30.07},
    {"id": 11, "survived": 1, "pclass": 3, "class": "Third", "name": "Sandstrom, Miss. Marguerite Rut", "sex": "female", "age": 4, "fare": 16.70},
    {"id": 12, "survived": 1, "pclass": 1, "class": "First", "name": "Bonnell, Miss. Elizabeth", "sex": "female", "age": 58, "fare": 26.55},
    {"id": 13, "survived": 0, "pclass": 3, "class": "Third", "name": "Saundercock, Mr. William Henry", "sex": "male", "age": 20, "fare": 8.05},
    {"id": 14, "survived": 0, "pclass": 3, "class": "Third", "name": "Andersson, Mr. Anders Johan", "sex": "male", "age": 39, "fare": 31.27},
    {"id": 15, "survived": 0, "pclass": 3, "class": "Third", "name": "Vestrom, Miss. Hulda Amanda Adolfina", "sex": "female", "age": 14, "fare": 7.85},
    {"id": 16, "survived": 1, "pclass": 2, "class": "Second", "name": "Hewlett, Mrs. (Mary D Kingcome)", "sex": "female", "age": 55, "fare": 16.00},
    {"id": 17, "survived": 0, "pclass": 2, "class": "Second", "name": "Williams, Mr. Charles Eugene", "sex": "male", "age": None, "fare": 13.00}
]
## q1 : number of survived passengers
# q2 : display unique passenger class 
# q3 number of female passengers
# q4: number of survived childs 
# q5: name whose fare > 30
# q6: number survived female
# q7:top fare
# q8 : survived peoples name
# q9:survived classes
# q10:female survival rate
survived_passengers=[di for di in titanic_data if di.get("survived")==1]
print(f"survived passengers {len(survived_passengers)}")
unique_passenger_class={di.get("class")for di in titanic_data}# here used set bcos of avoiding dupli
print(f"uniquepassnger class{unique_passenger_class}")
female_passenger=[di for di in titanic_data if di.get("sex")=="female"]
print(len(female_passenger))
#no of survived childs
num_survived_childs=[di for di in titanic_data if di.get("age") and di.get("age")<12 and di.get("survived")==1]
print(len(num_survived_childs))
fare_gt_30=[di.get("name")for di in titanic_data if di.get("fare")>30]
print(fare_gt_30)
number_survived_female=[di for di in titanic_data if di.get("survived")==1 and di.get("sex")=="female"]
print("no.ofsurvived females",len(number_survived_female))
#topfare
top_fare=max([di.get("fare")for di in titanic_data])
print("Top fare is",top_fare)
survived_people_name=[di.get("name")for di in titanic_data if di.get("survived")==1]
print("survived people names:",survived_people_name)
survived_classes={di.get("class")for di in titanic_data if di.get("survived")==1}
print("survived classes:",survived_classes)
# female survival rate
female_survived=[di for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
print("female survival rate",len(female_survived)/len(female_passenger)*100)


# number_survived_psngers=[di.get("survived")for di in titanic_data]
# print("length of survived passengers",len(number_survived_psngers))
# uni_pssnger_class={di.get("class")for di in titanic_data}
# print("unique passenger class",uni_pssnger_class)
# number_female_pssngers=[di for di in titanic_data if di.get("sex")=="female"]
# print("no.of female passengers",len(number_female_pssngers))
# number_survived_child=[di for di in titanic_data if di.get("age") and di.get("age")<14 and di.get("survived")==1]
# print(number_survived_child)
# names_of_fare_gt_thirty=[di.get("name")for di in titanic_data if di.get("fare")>30]
# print(names_of_fare_gt_thirty)
# number_of_survived_female=[di for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
# print("survived female number",len(number_of_survived_female))
# top_fare=(di.get("fare")for di in titanic_data)
# print("top faire is",max(top_fare))
# survived_peoplename=[di.get("name")for di in titanic_data if di.get("survived")==1]
# print("survived people name",survived_peoplename)
# survived_class=[di.get("class")for di in titanic_data if di.get("survived")==1]
# print(survived_class)
# femle_survivalrate=[di for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
# print("female survival rate",len(number_of_survived_female)/len(number_female_pssngers)*100)