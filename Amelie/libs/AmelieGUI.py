# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.label import Label

class AmelieApp(App):
    def build(self):
        return Label (text = "Amelie")

if __name__ == '__main__':
    AmelieApp().Run()
