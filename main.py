from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import time

class ClockApp(App):
    def build(self):
        self.label = Label(font_size=60)
        Clock.schedule_interval(self.update_time, 1)
        return self.label

    def update_time(self, *args):
        self.label.text = time.strftime('%H:%M:%S')

ClockApp().run()
