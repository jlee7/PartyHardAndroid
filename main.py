#!/usr/bin/env python2
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen

# IMPORT OWN CLASSES
from screenmanagement import *
from gamemodel import PartyHardGame
from eventmanager import *



__version__ = "1.6"


# LOADING THE KV FILE
game_kv = Builder.load_file("partyhard.kv")


class MainApp(App):
    screen_manager = ObjectProperty(None)

    def build(self):
        # Load assets at start up into memory
        bg2 = AsyncImage(source="assets/bg-2.jpg")

        self.eventmanager = EventManager()
        self.screen_manager = ScreenManagement(self.eventmanager)

        return self.screen_manager

if __name__ == "__main__":
    MainApp().run()
