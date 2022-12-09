import time
from Slave import Slave
from Master import Master

slaveObject = Slave()

masterObject = Master()

masterObject2 = Master()

slaveObject.buildTwoSecondEvent()
slaveObject.buildFiveSecondEvent()

masterObject.subscribeTwoSecondEvent()
masterObject.subscribeFiveSecondEvent()

masterObject2.subscribeTwoSecondEvent()
masterObject2.subscribeFiveSecondEvent()
i=0

while(True):
    if(i%2 == 0):
        slaveObject.eventTwoSecond()
    if(i%5 == 0):
        slaveObject.eventFiveSecond()
    time.sleep(1)
    i=i+1


