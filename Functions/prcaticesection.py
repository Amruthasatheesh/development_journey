#

#input="programming",output=3
# text="programming" 
# vowels="a,e,i,o,u"
# count=0
# for ch in text:
#     if ch in vowels:
#         count+=1
# print(count)
# reverse string without slicing

# text=input("enter string:")
# rev=0
# text_copy=text
# length=len(text) -1
# rev=rev+length
# if text_copy==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
data = {"a": 1, "b": 2, "c": 3}
keys = data.keys()
data["d"] = 4
print(list(keys))

values = [10, 20, 30, 40, 50]
print(values[::2])

str1 = "PYnative"
print(str1[0:-1])#pYnativ
print(str1[:-1])#pYnativ
print(str1[::-1])

def modify_list(items):
    items.append(4)
    return items

original_list = [1, 2, 3]
modified_list = modify_list(original_list)
print(original_list)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x*x, numbers))
print(squared_numbers)



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
