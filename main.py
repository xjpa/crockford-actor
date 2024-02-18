from multiprocessing import Process, Queue
import os

class Actor(Process):
    def __init__(self):
        super().__init__()
        # each actor has its own mailbox (queue)
        self.mailbox = Queue()  
        self.children = []
        # actors can have state
        self.state = None  

    def send(self, address, message):
        # send message to mailbox of another actor
        address.put(message)  

    def receive(self, message):
        """ process a message received by the actor. to be defined by subclass. """
        raise NotImplementedError

    def run(self):
        while True:
            message = self.mailbox.get()  # actors get messages from their mailbox
            if message == 'stop':
                for child in self.children:
                     # can send messages to stop child actors
                    child.send(child.mailbox, 'stop') 
                break
            self.receive(message)  # process the received message

    def create_actor(self, actor_class):
        child = actor_class()
        child.start()  # start the actor's process
        self.children.append(child)
        return child.mailbox  # return the address of the new actor

    def stop(self):
        self.send(self.mailbox, 'stop')  # send stop message to itself

class PrintingActor(Actor):
    def __init__(self):
        super().__init__()
        # actor keeps a list as its state
        self.state = []  

    def receive(self, message):
        if isinstance(message, str):
            print(f"Actor {os.getpid()} received message: {message}")
            # update the state based on the message
            self.state.append(message)  
        elif isinstance(message, tuple):
            target_address, target_message = message
            # can send messages to other actors
            self.send(target_address, target_message)  