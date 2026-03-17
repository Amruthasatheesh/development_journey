class Shapes:
    def area(self,*args):
        if len(args)==1:
            r=args[0]
            print("area of circle ",3.14*r**2)
        elif len(args)==2:
           l=args[0]
           b=args[1]
           print("area of rectangle",l*b)
        elif len(args)==3:
            l=args[0]
            b=args[1]
            h=args[2]
            print("area of cuboid",l*b*h)
shape_instance=Shapes()
shape_instance.area(10)
shape_instance.area(10,20)
shape_instance.area(10,2,5)
    