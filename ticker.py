from kivy.clock import Clock
from eventmanager import *

class Ticker:
    def __init__(self):
        pass
        #self.event_manager = EventManager()
        #self.event_manager.register_listener(self)

    def notify(self, event):
        if isinstance (event, TickEvent):
            print "Ticking in the Ticker"
        elif isinstance (event, CollisionEvent):
            pass
        elif isinstance (event, PartyTimeSwitch):
            pass
        elif isinstance(event, StopGameEvent):
            pass
        elif isinstance(event, RestartGameEvent):
            pass

    def send_ticks(self, dt):
        print "Ticker fired"
        self.event_manager.post(TickEvent())
        

    def start_ticker(self, command):
        Clock.schedule_interval(command, 1.0 / 60.0)
        #Clock.schedule_interval(self.game.update, 1.0 / 60.0)
        print "Starting ticker"

    def stop_ticker(self, command):
        Clock.unschedule(command, True)

    def printstuff(self):
        print "STUFF"

time_controller = Ticker()
