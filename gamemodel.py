from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from eventmanager import *

# IMPORT OWN CLASSES
from objectclasses import RandomItem, PartyDude
import gameaudio

class PartyHardGame(Widget):
    dude = ObjectProperty(None)
    displayed_mode = ObjectProperty(None)
    displayed_time = ObjectProperty(None)
    displayed_score = ObjectProperty(None)

    move_right = BooleanProperty(False)
    move_left = BooleanProperty(False)
    timer = NumericProperty(0)
    countdown = NumericProperty(30)
    score_text = NumericProperty(0)
    partytime = BooleanProperty(True)
    game_is_running = BooleanProperty(True)
    timer = NumericProperty(0)
    background_partytime = "assets/bg-1.jpg"
    background_studytime = "assets/bg-2.jpg"


    # def __init__(self, eventmanager):
    #     super(PartyHardGame, self).__init__()
    #     # Register to Event Manager
    #     self.eventmanager = eventmanager
    #     self.eventmanager.register_listener(self)


    # def notify(self, event):
    #     if isinstance (event, TickEvent):
    #         print "Ticking in the game model"
    #         self.update()
    #     elif isinstance (event, CollisionEvent):
    #         pass
    #     elif isinstance (event, PartyTimeSwitch):
    #         pass
    #     elif isinstance(event, StopGameEvent):
    #         pass
    #     elif isinstance(event, RestartGameEvent):
    #         pass

    def testing(self):
        print "Mode:", self.displayed_mode.text
        print "Score:", self.displayed_score.text
        print "Time:", self.displayed_time.text
        print "Move right:", self.move_right
        print "Move left:", self.move_left
        print "Timer:", self.timer
        print "Countdown:", self.countdown
        print "Score text:", self.score_text
        print "Partytime:", self.partytime

    def reset_game_stats(self):
        print "resetting game"
        self.countdown = 30
        self.score_text = 0
        self.partytime = True
        self.timer = 0
        self.update_score()
        for child in self.children:
            if isinstance(child, RandomItem):
                self.remove_widget(child)
                print "removing child"

    def spawn(self):
        new_item = RandomItem()
        self.add_widget(new_item)
        new_item.set_look()

    def toggle_mode(self):
        if self.partytime == True:
            self.partytime = False
            self.canvas.children[1].source = self.background_studytime
            self.displayed_mode.text = "Study Time!"
            gameaudio.sound_studytime.play()
        else:
            self.partytime = True
            self.canvas.children[1].source = self.background_partytime
            self.displayed_mode.text = "Party Time!"
            gameaudio.sound_partytime.play()

        for child in self.children:
        #---self.children also contains the Dude, so distinguish
            if isinstance(child, RandomItem):
                child.set_look()
        #self.testing()

    def update(self, dt):
        if self.game_is_running:
            self.timer += 1
            # Weil ich die size_x nicht wusste
            size_x, size_y = self.size
            dude_x, dude_y = self.dude.size
      
            #------MOVEMENT OF DUDE
            if self.move_right:
                if self.dude.center_x > 0 + dude_x / 2:
                    #self.dude.center_x -= 5
                    self.dude.center_x -= Window.height / 100
                else:
                    pass

            elif self.move_left:
                #print "LEFT"
                if self.dude.center_x < size_x - dude_x / 2:
                    #self.dude.center_x += 5
                    self.dude.center_x += Window.height / 100
                else:
                    pass

            #-------SPAWN OF ITEMS
            if self.timer % 10 == 0:
                self.spawn()

            #-------MOVEMENT OF EACH ITEM
            for child in self.children:
            #---self.children also contains the Dude, so distinguish
                if isinstance(child, RandomItem):
                    child.move()

            #---------------DELETE ALL ITEMS BELOW Y=0 (Groud Zero)
                    if child.y < 0 - child.height:
                        self.remove_widget(child)
                        #print "items removed because too low"

            #-------COLLLISON OF ITEM WITH DUDE
            self.dude.check()

            #-------COUNT DOWN GAME TIME
            self.displayed_time.text = str(self.countdown - self.timer / 60)

            #-------TOGGLE MODE
            if self.timer % 300.0 == 0:
                self.toggle_mode()

            #-------CHECK IF TIME IS GONE
            if (self.countdown - self.timer / 60) == 0:
                print "time is up"

                for child in self.children:
                    if isinstance(child, RandomItem):
                        self.remove_widget(child)
                        print "removing child"

                self.parent.parent.current = "end_screen"


    def update_score(self):
        self.displayed_score.text = str(self.score_text)


    def on_touch_down(self, touch):
        if touch.x < self.width / 3:
            self.move_right = True

        elif touch.x > self.width - self.width / 3:
            self.move_left = True



    def on_touch_up(self, touch):
        self.move_right = False
        self.move_left = False