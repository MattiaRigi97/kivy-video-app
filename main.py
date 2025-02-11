import kivy

#kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button

class ScreenTwo(Screen):
    def test_on_enter(self, vidname):
        #self.add_widget(Button(text="Back"))
        self.vid = VideoPlayer(source=vidname, state='play',
                               options={'allow_stretch':False,
                                        'eos': 'loop'})
        self.add_widget(self.vid)

    def on_leave(self):
        pass

    def onBackBtn(self):
        self.vid.state = 'stop'
        self.remove_widget(self.vid)
        self.manager.current = self.manager.list_of_prev_screens.pop()

class ScreenOne(Screen):
    def onNextScreen(self, btn, fileName):
        self.manager.list_of_prev_screens.append(btn.parent.name)
        self.manager.current = 'screen2'
        self.manager.screen_two.test_on_enter(r"C:\Users\matti\github\kivy-video-app\Resources\Videos\sample1.mp4")

class Manager(ScreenManager):
    transition = NoTransition()
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        # list to keep track of screens we were in
        self.list_of_prev_screens = []

class ScreensApp(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    ScreensApp().run()