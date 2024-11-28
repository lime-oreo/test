from abc import ABC, abstractmethod

class Vehicle (ABC):
    def getOn(self):
        print ("getting on the vehicle")

    def getOff(self):
        print ("Getting off the vehicle")
    

class Transferable(ABC):
    @abstractmethod
    def transfer(self):
        pass

class Bus(Vehicle, Transferable): #Transferable을 상속받음
    def transfer (self):
        print ("Transfered to another subway or bus")

class Subway(Vehicle,Transferable):
    def transfer (self):
        print ("Transfered to another subway or bus")
    
class Taxi (Vehicle):
    pass

if __name__=="__main__":
    bus = Bus()
    subway = Subway()
    taxi = Taxi()

    bus.getOn()
    subway.getOn()
    taxi.getOn()

    bus.getOff()
    subway.getOff()
    taxi.getOff()

    bus.transfer()
    subway.transfer()

else :
    print ('다른 모듈에서 호출했음')