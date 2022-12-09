# ksubscribe-example-usage
ksubscribe-example-usage

## Example code 
Usage : python main.py
<br/><br/>
In this example usage of ksubscribe we have Master and Slave class.
<br/>
2 Master object subscribe same events, one event takes parameters, one event does not take params.
<br/>
One of this event is everyTwoSecond, that is fired every two second and do not take parameters
<br/>
The other event is everyFiveSecond, that is fired every five second and take parameter.<br/><br/>
:raising_hand: <br/><br/>:exclamation: 

#### For not taking any parameters event, subscribers must have _**_inform(eventName:str)**_ functions. 

<br/><br/>:exclamation:

#### For taking parameters event, subscribers must have _**_inform(eventName:str,parameters)**_ functions. You can send only one parameter, that can be string, int, list, dict etc.

<br/><br/>
You can easily understand basic usage of the library from this repository.
<br/><br/>
If you have any question, you can send me email that is mentioned in below.
<br/><br/>
Email : kuzucu48@gmail.com