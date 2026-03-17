#should include all the methods from abstract base class to inherted class


from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def transmission(self):pass
    @abstractmethod
    def start(self):pass

class Pulsar(Bike):
    def transmission(self):
        print("pulsar transmission method")
    def start(self):
        print("pulsar starting method")

pulsar_instance=Pulsar()
pulsar_instance.transmission()
pulsar_instance.start()

