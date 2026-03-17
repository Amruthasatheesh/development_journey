fr=open("Nested collection\\flight.txt","r")
flight_list=[]
for line in fr:
    data=line.rstrip("\n").split(",")
    flight_dict={"year":data[0],"month":data[1],"passangers":int(data[2])}
    flight_list.append(flight_dict)
print(flight_list)
#year as key and passenger count sum of each hyear
year_wise_count = {} 

for f in flight_list:
    
    year = f.get("year")
    
    p_count = f.get("passangers")
    
    if year in  year_wise_count:
        
        year_wise_count[year]+=p_count
        
    else:
        
        year_wise_count[year]=p_count
print(year_wise_count)
        
# sorted_flight = sorted([{v,k} for k,v in year_wise_count.items()])
# print(sorted_flight)

# #or
# print("**********")
# year_wise_sorted = sorted(year_wise_count,key = year_wise_count.get)
# print(year_wise_sorted)