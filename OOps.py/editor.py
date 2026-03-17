from abc import ABC,abstractmethod

class Editor(ABC):
    @abstractmethod
    def open(self):pass
    @abstractmethod
    def execute(self):pass
    @abstractmethod
    def debug(self):pass

class Vscode(Editor):
    def open(self):
        print("open method of vscode")
    def execute(self):
        print("execute method of vscode")
    def debug(self):
        print("debug method of vscode") 

vs_instance=Vscode()
vs_instance.open()  
vs_instance.execute()  
vs_instance.debug()  