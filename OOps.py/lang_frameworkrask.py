class Language:
    def __init__(self,lanname):
        self.lanname=lanname
    def display(self):
        print(self.lanname)

class Framework(Language):
    def __init__(self,lanname,frname):
        super().__init__(lanname)
        self.frname=frname
    def display(self):
        super().display()
        print(self.frname)

frame_instance1=Framework("python","django")
frame_instance2=Framework("python","flask")
frame_instance3=Framework("python","oodo")
frame_instance1.display()
frame_instance2.display()
frame_instance3.display()