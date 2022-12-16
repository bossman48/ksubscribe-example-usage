import time
from Slave import Slave
from Master import Master

slaveObject = Slave()

masterObject = Master()

masterObject2 = Master()

slaveObject.buildTwoSecondEvent()
slaveObject.buildFiveSecondEvent()

masterObject.subscribeAnEvent("everyTwoSecond")
masterObject.subscribeAnEvent("everyFiveSecond")

masterObject2.subscribeAnEvent("everyTwoSecond")
masterObject2.subscribeAnEvent("everyFiveSecond")
i=0



while(True):
    if(i%2 == 0):
        slaveObject.eventTwoSecond()
    if(i%5 == 0):
        slaveObject.eventFiveSecond()
    time.sleep(1)
    if(i>0 and i%13 == 0):
        masterObject.deleteSubscription(eventName="everyTwoSecond")
    
    if(i>0 and i%17 == 0):
        masterObject.deleteAnEvent(eventName="everyTwoSecond")

    if(i>0 and i%23 == 0):
        masterObject.deleteAllEvents()
    i=i+1


