def calculator(*args,**kwargs):
    if kwargs.get("key")=="+":
        return sum(args)
    if kwargs.get("key")=="*":
        p=1
        for num in args:
            p=p*num
        return p

print(calculator(10,20,30,40,key="+"))
print(calculator(10,20,30,40,key="*"))

# def analyze_numbers(*args,**kwargs):
#     if kwargs.get("action")=="max":
#         return max(args)
#     if kwargs.get("action")=="min":
#         return min(args)
#     if kwargs.get("action")=="count":
#         return len(args)
    
# print(analyze_numbers(10,11,12,13,14,15,action="max"))
# print(analyze_numbers(10,11,12,13,14,15,action="min"))
# print(analyze_numbers(10,11,12,13,14,15,action="count"))

def number_checker(*args,**kwargs):
    type=kwargs.get("type")
    if type=="odd":
        odd=len([num for num in args if num%2!=0])
        return odd
    elif type=="even":
        even=len([num for num in args if num%2==0])
        return even
    elif type=="positive":
        positive=len([num for num in args if num>0])
        return positive
    elif type=="negative":
        negative=len([num for num in args if num<0])
        return negative
    
print(number_checker(10,11,12,13,14,15,type="odd"))
print(number_checker(10,11,12,13,14,15,type="even"))
print(number_checker(10,11,12,13,14,15,type="positive"))
print(number_checker(10,11,12,13,-14,-15,type="negative"))

def mark_calculator(*args,**kwargs):
    option=kwargs.get("options")