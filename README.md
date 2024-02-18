Actor Model

required

- at 19:00: https://www.youtube.com/watch?v=vMDHpPN_p08
- an actor is a program running in a single process in a machine
- an actor communicates with other actors only be message passing
- there is no sharing, even between actors in the same machine
- an actor can create new actors in its own machine
- every actor has a private address
- if you have an actor's private address, you can send messages to that actor
- messages can contain private addressses
- actors can have state, which can change based on received messages

recommended

- incoming messagse are queued if necessary, delivered in arrival order
- an actor will not be given another message until it is done
- messages sent by an actor will be held until it is done
- an actors turn may be timesliced
