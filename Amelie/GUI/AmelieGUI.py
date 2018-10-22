# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.anchorlayout import AnchorLayout

from kivy.properties import ListProperty
from kivy.config import Config

Config.set('graphics', 'resizable', 0)

class Header(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(.53, .19, .71, 1)
            Rectangle(pos=self.pos, size=self.size)

class AmelieApp(App):
    def build(self):
        
         
        al = AnchorLayout(anchor_x = 'center', anchor_y = 'top')
        label = Header(
            text='Amelie',
            color = [.66, .57, .71, 1],
            font_size = 50,
            pos=(100, 100),
            size_hint=(1, 0.3))
        al.add_widget(label)

        

        return al



if __name__ == '__main__':
    AmelieApp().run()