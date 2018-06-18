from sys import exit
from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class LightButton(Button):
    pass


class ExitButton(Button):
    pass


class BackButton(Button):
    pass


class HomeScreen(Screen):
    def close_gui(self):
        exit()


class LightScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.transition = NoTransition()
        sm.add_widget(HomeScreen(name='Home'))
        sm.add_widget(LightScreen(name='Lights'))
        return sm


if __name__ == "__main__":
    app = MainApp().run()
