#DICTIONARY
"""
dictionary={key:value,key:value}
value accesed using key

"""
employee={"name":"vipin","dpt":"hr","workplace":"kakanad","salary":"340000"}
#accesing value
print(employee["salary"])
# update a key
employee["dpt"]="Associate engineer"
print(employee)


#create a dictionary of product with attribute
#id,title,price,avl_quantity
book={"id":101,"title":"subconcious mind","price":150,"avl_quantity":20}
print(book)
#change the avl_quanity  50 in to 60 
book["avl_quantity"]+=10
print(book)
#add an key:value ,if its already exist just updating the code value
book["code"]="sku12"
print(book)
#To check the existance of the key using "in" operator
book={"id":101,"title":"subconcious mind","price":150,"avl_quantity":20}
if "title" in book:
    print("yes")
else:
    print("no")