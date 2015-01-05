from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from libs.convnz import fz
from libs.convnz import iz


class TitleScreen(Screen):
    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)


class JapaneseCalcScreen(Screen):
    score_b = StringProperty('0')
    score_w = StringProperty('0.0')

    def calc_score(self):
        self.score_b = str(iz(self.ids.terr_b.text) +
                           iz(self.ids.pris_b.text) +
                           (2 * iz(self.ids.dead_w.text)))
        self.score_w = str(iz(self.ids.terr_w.text) +
                           iz(self.ids.pris_w.text) +
                           (2 * iz(self.ids.dead_b.text)) +
                           fz(self.ids.komi.text))


class ChineseCalcScreen(Screen):
    score_b = StringProperty('0')
    score_w = StringProperty('0.0')

    def calc_score(self):
        self.score_b = str(iz(self.ids.terr_b.text) +
                           iz(self.ids.ston_b.text) +
                           iz(self.ids.dead_w.text))
        self.score_w = str(iz(self.ids.terr_w.text) +
                           iz(self.ids.ston_w.text) +
                           iz(self.ids.dead_b.text) +
                           fz(self.ids.komi.text))