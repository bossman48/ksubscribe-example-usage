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

    def _inform(self,eventName):
        print("From ",id(self)," _inform function",eventName)

    def _informWithParameter(self,eventName,parameters):
        print("From ",id(self)," _informWithParameter function",eventName,"  ",parameters)