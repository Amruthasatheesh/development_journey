"""**kwargs accept as dictonary """

def employee(**kwargs:dict): #{"name":"hari","dept":"hr","salary"=30000}
    print(kwargs)
    print(kwargs.get("name"))
    print(kwargs.get("dept"))
    print(kwargs.get("salary"))

employee(name="hari",dept="Hr",salary=30000)