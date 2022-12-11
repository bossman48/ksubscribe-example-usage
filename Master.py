import time
from ksubscribe import Ksubscribe 

class Master():

    def __init__(self):
        self.masterEventObject = Ksubscribe()
        print("Master Ksubscribe Object id :", id(self.masterEventObject))

    def subscribeTwoSecondEvent(self):
        self.masterEventObject._subscribeForAnEvent(subscriber=self,eventName="everyTwoSecond")

    def subscribeFiveSecondEvent(self):
        self.masterEventObject._subscribeForAnEvent(subscriber=self,eventName="everyFiveSecond")

    def inform(self,eventName,parameters=None):
        if(parameters==None):
            print("From ",id(self)," inform function",eventName)
        else:
            print("From ",id(self)," inform function",eventName, " with this parameters : ",parameters)