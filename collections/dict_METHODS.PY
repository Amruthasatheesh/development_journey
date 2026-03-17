"""
class dict:
     def keys(self):return all keys
     def values(self):return values
     def items(self):return key :value pairs
     def get(self,key):return the value
     def pop(self,key):remove key:value
"""

employee={"id":101,"name":"vipin","salary":75000,"dept":"qa"}
for key in employee.keys():# for getting all the keys
    print(key)

employee={"id":101,"name":"vipin","salary":75000,"dept":"qa"}
for val in employee.values():
    print(val)
for k ,v in employee.items():
    print(k,v)

#To get the value using get() method
print(employee.get("name"))
# returns none if we give the not existing key
print(employee.get("names"))
# if email key not existed,it retuns the dummy@gmail.com(better to choose this get( method instead of using employee["name"]))
print(employee.get("email","dummy@gmail.com"))
print("line 1")
#to remove specific key using pop()
print(employee.pop("dept"))# here giving print() in ist line to show which one is removed here, if we need to know in any case
print(employee)
#adding value
employee["bonus"]=5000
print(employee)
#to update the value in key
employee["bonus"]+=10000
print(employee)