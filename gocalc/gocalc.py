#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from libs.convnz import fz
from libs.convnz import iz


class GoCalc(BoxLayout):
    def calc_score(self, terr, pris, dead, komi=0):
        '''
        :param terr: territory as string or int
        :param pris: prisoners as string or int
        :param dead: dead stones as string or int
        :param komi: komi as string or float
        :return: score as string
        '''
        return(str(iz(terr) + iz(pris) + (2 * iz(dead)) + fz(komi)))


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
