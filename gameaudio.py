from kivy.core.audio import SoundLoader

class MultiAudio:
    _next = 0

    def __init__(self, filename, count):
        self.buf = [SoundLoader.load(filename)
                    for i in range(count)]

    def play(self):
        self.buf[self._next].play()
        self._next = (self._next + 1) % len(self.buf)

# Load assets at start up
# BGM
sound_start_screen = SoundLoader.load("assets/rock.ogg")
sound_start_screen.loop = True
sound_game_screen = SoundLoader.load("assets/rock2.ogg")
sound_game_screen.loop = True
sound_end_screen = SoundLoader.load("assets/dream.ogg")
sound_end_screen.loop = True

# FX
sound_item_catch_red1 = MultiAudio("assets/mmmh.ogg", 5)
sound_item_catch_red2 = MultiAudio("assets/no.ogg", 5)
#sound_item_catch_red3 = MultiAudio("", 1)
sound_item_catch_green1 = MultiAudio("assets/yeah.ogg", 5)
#sound_item_catch_green2 = MultiAudio("", 1)
sound_partytime = SoundLoader.load("assets/partytime.ogg")
sound_studytime = SoundLoader.load("assets/studytime.ogg")