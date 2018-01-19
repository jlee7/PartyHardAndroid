from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import gameaudio
#import ticker
from kivy.clock import Clock

class StartScreen(Screen):
    def on_enter(self):
        gameaudio.sound_start_screen.play()

    def on_pre_leave(self):
        gameaudio.sound_start_screen.stop()


class GameScreen(Screen):
    game = ObjectProperty(None)
    
    def on_enter(self):
        self.game.reset_game_stats()
        gameaudio.sound_game_screen.play()
        self.ids.party_hard_game.game_is_running = True
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)
        #ticker.time_controller.start_ticker(ticker.time_controller.send_ticks)


    def on_pre_leave(self):
        Clock.unschedule(self.game.update, True)
        gameaudio.sound_game_screen.stop()


class EndScreen(Screen):
    displayed_points = ObjectProperty(None)

    
    def on_enter(self):
        gameaudio.sound_end_screen.play()
        if self.parent.g_screen.game.displayed_score.text:
            self.displayed_points.text = "Points: %s" %(self.parent.g_screen.game.displayed_score.text)
        else:
            self.displayed_points.text = "No points! Play again?"
        # print self.ids
        # print self.parent
        # print self.parent.g_screen
        # print self.parent.g_screen.children
        # print self.parent.g_screen.game.displayed_score.text


    def on_pre_leave(self):
        gameaudio.sound_end_screen.stop()


class CreditScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    def __init__(self, eventmanager):
        super(ScreenManagement, self).__init__()

        #self.eventmanager = eventmanager
        #self.eventmanager.register_listener(self)

        self.s_screen = StartScreen(name="start_screen")
        self.g_screen = GameScreen(name="game_screen")
        self.e_screen = EndScreen(name="end_screen")
        self.c_screen = CreditScreen(name="credits")
        self.add_widget(self.s_screen)
        self.add_widget(self.g_screen)
        self.add_widget(self.e_screen)
        self.add_widget(self.c_screen)

        print self.g_screen
        print dir(self)

    # def notify(self, event):
    #     if isinstance (event, TickEvent):
    #         print "Ticking in Screenmanager"
    #     elif isinstance (event, CollisionEvent):
    #         pass
    #     elif isinstance (event, PartyTimeSwitch):
    #         pass
    #     elif isinstance(event, StopGameEvent):
    #         pass
    #     elif isinstance(event, RestartGameEvent):
    #         pass