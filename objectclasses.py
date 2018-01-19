import random
from kivy.uix.widget import Widget
from kivy.core.window import Window
import gameaudio

class RandomItem(Widget):
    
    def __init__(self):
        super(RandomItem, self).__init__()
        random_position_x = random.randrange(0, Window.width - self.width)
        fixed_position_y = Window.height
        self.pos = (random_position_x, fixed_position_y)
        self.size = Window.height / 10, Window.height / 10
        self.item = random.randrange(1,5)
        self.item_already_eaten = False
        self.movement_speed = Window.height / random.randrange(80, 110)

    def set_look(self):
        if self.parent.partytime:
            if self.item == 1:
                self.canvas.children[1].source = "assets/item-cocktail_green.png"
            elif self.item == 2:
                self.canvas.children[1].source = "assets/item-six-pack_green.png"
            elif self.item == 3:
                self.canvas.children[1].source = "assets/item-book_red.png"
            elif self.item == 4:
                self.canvas.children[1].source = "assets/item-laptop_red.png"
        else:
            if self.item == 1:
                self.canvas.children[1].source = "assets/item-cocktail_red.png"
            elif self.item == 2:
                self.canvas.children[1].source = "assets/item-six-pack_red.png"
            elif self.item == 3:
                self.canvas.children[1].source = "assets/item-book_green.png"
            elif self.item == 4:
                self.canvas.children[1].source = "assets/item-laptop_green.png"

        #print "Setting item appearance"

    def toggle_score(self):
        if self.parent.partytime:
            if self.item == 1 or self.item == 2:
                gameaudio.sound_item_catch_green1.play()
                self.canvas.children[1].source = "assets/score_plus.png"
                self.parent.score_text += 10
            elif self.item == 3 or self.item == 4:
                [gameaudio.sound_item_catch_red1, gameaudio.sound_item_catch_red2][random.randint(0,1)].play()
                self.canvas.children[1].source = "assets/score_minus.png"
                self.parent.score_text -= 5
        else:
            if self.item == 1 or self.item == 2:
                [gameaudio.sound_item_catch_red1, gameaudio.sound_item_catch_red2][random.randint(0,1)].play()
                self.canvas.children[1].source = "assets/score_minus.png"
                self.parent.score_text -= 5
            elif self.item == 3 or self.item == 4:
                gameaudio.sound_item_catch_green1.play()
                self.canvas.children[1].source = "assets/score_plus.png"
                self.parent.score_text += 10
        self.parent.update_score()

        self.item_already_eaten = True


    def move(self):
        self.y -= self.movement_speed


class PartyDude(Widget):
    def __init__(self, **kwargs):
        super(PartyDude, self).__init__(**kwargs)
        self.dude_hands_down = "assets/party-dude.png"
        self.dude_hands_up = "assets/party-dude-hands-up.png"
        self.hands_up_duration = 60
        self.hands_up_counter = 0
        self.arms_are_up = False
        self.counter = 0


    def toggle_arms_up(self):
        self.canvas.children[1].source = "assets/party-dude-hands-up.png"


    def toggle_arms_down(self):
        self.canvas.children[1].source = "assets/party-dude.png"


    def check(self):
        try:
            for child in self.parent.children:
                if isinstance(child, RandomItem):
                    if self.collide_widget(child):
                        self.counter += 1
                        if self.arms_are_up == False:
                            self.toggle_arms_up()
                            self.arms_are_up = True
                            child.toggle_score()
                            #self.parent.update_score()

                        if self.counter == 6:
                            self.parent.remove_widget(child)
                            self.toggle_arms_down()
                            self.arms_are_up = False
                            self.counter = 0
        except Exception as e:
            print e