#qpy:2
#qpy:kivy
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage

from kivy.uix.screenmanager import ScreenManager, Screen

# IMPORT OWN CLASSES
from screenmanagement import *
from gamemodel import PartyHardGame
from eventmanager import *
#from ticker import *
#from gameaudio import *
#from gamemodel import *


__version__ = "1.6"


# LOADING THE KV FILE
game_kv = Builder.load_file("partyhard.kv")


class MainApp(App):
    screen_manager = ObjectProperty(None)

    def build(self):
        # Load assets at start up into memory
        bg2 = AsyncImage(source="assets/bg-2.jpg")

        self.eventmanager = EventManager()


        #self.the_game = PartyHardGame(self.eventmanager)
        self.screen_manager = ScreenManagement(self.eventmanager)
        # self.screen_manager = ScreenManager()
        # s_screen = StartScreen(name="start_screen")
        # g_screen = GameScreen(name="game_screen")
        # e_screen = EndScreen(name="end_screen")
        # c_screen = CreditScreen(name="credits")
        # self.screen_manager.add_widget(s_screen)
        # self.screen_manager.add_widget(g_screen)
        # self.screen_manager.add_widget(e_screen)
        # self.screen_manager.add_widget(c_screen)
        return self.screen_manager

if __name__ == "__main__":
    MainApp().run()
