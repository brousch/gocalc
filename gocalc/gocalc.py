#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput

from screens import TitleScreen
from screens import JapaneseCalcScreen
from screens import ChineseCalcScreen


class GoCalc(BoxLayout):
    def __init__(self, **kwargs):
        super(GoCalc, self).__init__(**kwargs)
        self.content = ScreenManager()
        self.content.transition = FadeTransition()
        self.content.add_widget(TitleScreen(name='Title'))
        self.content.add_widget(JapaneseCalcScreen(name='JapaneseCalc'))
        self.content.add_widget(ChineseCalcScreen(name='ChineseCalc'))
        self.add_widget(self.content)


class StoneInput(TextInput):
    def focus_changed(self):
        '''
        If focus is entering, select all the text.
        If focus is leaving, deselect everything.
        '''
        if self.focus:
            Clock.schedule_once(lambda dt: self.select_all())
        else:
            self.cancel_selection()


class GoCalcApp(App):
    def build(self):
        return GoCalc()

    def on_pause(self):
        return True

    def on_resume(self):
        pass
