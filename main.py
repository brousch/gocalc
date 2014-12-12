#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


__version__ = '0.0.1'


class GoCalc(BoxLayout):
    def iz(self, x):
        try:
            return int(x)
        except:
            return 0

    def fz(self, x):
        try:
            return float(x)
        except:
            return 0


class GoCalcApp(App):
    def build(self):
        return GoCalc()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    GoCalcApp().run()