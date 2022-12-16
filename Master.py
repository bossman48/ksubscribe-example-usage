import time
from ksubscribe import Ksubscribe 

class Master():

    def __init__(self):
        self.masterEventObject = Ksubscribe()
        print("Master Ksubscribe Object id :", id(self.masterEventObject))

    def subscribeAnEvent(self,eventName:str):
        self.masterEventObject._subscribeForAnEvent(subscriber=self,eventName=eventName)

    def inform(self,eventName,parameters=None):
        if(parameters==None):
            print("From ",id(self)," inform function",eventName)
        else:
            print("From ",id(self)," inform function",eventName, " with this parameters : ",parameters)

    def deleteSubscription(self,eventName:str):
        print("Delete subscription with event : ", eventName)
        self.masterEventObject._removeSubscriberFromEvent(self,eventName)

    def deleteAllEvents(self):
        print("Delete all events : ")
        self.masterEventObject._removeAllEvents()

    def deleteAnEvent(self,eventName:str):
        print("Delete the event : ", eventName)
        self.masterEventObject._removeAnEvent(eventName=eventName)