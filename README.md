# ksubscribe-example-usage
ksubscribe-example-usage


#### In this example usage of ksubscribe we have Master and Slave class.
#### 2 Master object subscribe same events, one event takes parameters, one event does not take params.
#### One of this event is everyTwoSecond, that is fired every two second and do not take parameters
#### The other event is everyFiveSecond, that is fired every five second and take parameter.


## For not taking any parameters event, subscribers must have _inform(eventName:str) functions. 

## For taking parameters event, subscribers must have _inform(eventName:str,parameters) functions. 


#### You can easily understand basic usage of the library from this repository.

#### If you have any question, you can send me email that is mentioned in below.

Email : kuzucu48@gmail.com