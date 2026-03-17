fr=open("file_operations\\orders.txt","r")
orders_list=[]
for line in fr:
    cleaned_line=line.rstrip("\n")
    orders_list.append(cleaned_line)
orders_count={o:orders_list.count(o) for o in orders_list}
print(orders_count)