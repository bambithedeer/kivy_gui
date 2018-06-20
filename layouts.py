from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty


class HomeGrid(GridLayout):

    numButtons = NumericProperty()
    maxButtons = NumericProperty()
    minButtons = NumericProperty()


