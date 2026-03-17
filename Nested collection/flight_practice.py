
fr=open("Nested collection\\flight.txt","r")
flight_list=[]
for line in fr:
    data=line.rstrip("\n").split(",")
    data_dict={"year":data[0],"month":data[1],"passenger":int(data[2])}
    flight_list.append(data_dict)
print(flight_list)
#year wise count of passengers in each year
year_wise_count={}
for f in flight_list:
    year=f.get("year")
    p_count=f.get("passenger")
    if year in year_wise_count:
        year_wise_count[year]+=p_count
    else:
        year_wise_count[year]=p_count
    print("year wise count",year_wise_count)

sorted_year_wise=sorted({v,k}for k,v in year_wise_count.items())
print("sorted count",sorted_year_wise)
    