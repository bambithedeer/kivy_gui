from kivy.uix.gridlayout import GridLayout


class HomeGrid(GridLayout):
    def __init__(self):
        super(HomeGrid, self).__init__()
        self.cols = 4
        self.rows = 4
