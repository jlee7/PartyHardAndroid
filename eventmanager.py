from weakref import WeakKeyDictionary


#----------------------------------------------------------------------

class EventManager(object):

    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.last_tick = 0

    #----------------------------------------------------------------------

    def register_listener(self, listener):
        print listener, "is listening to the event manager!", self
        self.listeners[listener] = True

    #----------------------------------------------------------------------

    def post(self, event):

        if (not isinstance (event, TickEvent) 
            and not isinstance (event, DudeMoveEvent) 
            and not isinstance (event, CollisionEvent) 
            and not isinstance (event, ItemCatchPositive) 
            and not isinstance (event, ItemCatchNegative) 
            and not isinstance (event, SpawnItemEvent)):
            print "Event: " + event.name + " (" + str(self.last_tick) + ")"
        elif isinstance (event, TickEvent):
            print "Tickevent in Eventmanager"

        for listener in self.listeners:
            print listener,
            listener.notify(event)

    #----------------------------------------------------------------------

    def test(self):
        print "Testausgabe"

#----------------------------------------------------------------------

class Event(object):
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "Timer Tick"

class DudeMoveEvent(Event):
    def __init__(self, direction):
        self.name = "Dude Move"
        self.direction = direction

class SpawnItemEvent(Event):
    def __init__(self, item):
        self.item = item
        self.name = "Spawn Item " + item.__class__.__name__

class CollisionEvent(Event):
    def __init__(self, item):
        self.item = item
        self.name = "CollisionEvent Item " + item.__class__.__name__

class PartyTimeSwitch(Event):
    def __init__(self):
        self.name = "Switch Party Time"

class StopGameEvent(Event):
    def __init__(self):
        self.name = "Stop Game"

class RestartGameEvent(Event):
    def __init__(self):
        self.name = "Restart Game"

class ItemCatchPositive(Event):
    def __init__(self):
        self.name = "Positive Item Catch"

class ItemCatchNegative(Event):
    def __init__(self):
        self.name = "Negative Item Catch"
