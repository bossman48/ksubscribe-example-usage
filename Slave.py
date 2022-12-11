
from ksubscribe import Ksubscribe 

class Slave():

    def __init__(self):
        self.slaveEventObject = Ksubscribe()
        print("Slave Ksubscribe object id :",id(self.slaveEventObject))

    def buildTwoSecondEvent(self):
        self.slaveEventObject._createAnEvent(eventName="everyTwoSecond")

    def buildFiveSecondEvent(self):
        self.slaveEventObject._createAnEvent(eventName="everyFiveSecond")


    def eventTwoSecond(self):
        self.slaveEventObject._publish(eventName="everyTwoSecond")

    def eventFiveSecond(self):
        self.slaveEventObject._publish(eventName="everyFiveSecond",parameters=["ksubscribe","for","Python","Coders"])
        

        
    

