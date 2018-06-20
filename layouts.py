from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty


class HomeGrid(GridLayout):
    maxButtons = NumericProperty()
    numButtons = NumericProperty()
    minButtons = NumericProperty()

    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)
        self.cols = 4
        self.row = 4
        self.maxButtons = 16
        self.minButtons = 3
        self.numButtons = 3
        self.id = "base_grid"


