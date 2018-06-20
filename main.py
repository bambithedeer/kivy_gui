'''
Author: Andrew Baumbach
Description: Gui to be run on custom sopine armbian tablet
Version history:
    6/17/2018 - Base revision - Figured out how to structure everything, added basic settings app for
        tablet backlight, add page for house light app, added future functionality tags
Project TODOs-
    Setup server and data base
    Make a plan for communication between tablet and system
    !!!! Virtual Keyboard / Keypad !!!!!
    Design light system
    Possible audio support through google homes and spotify / Music app
    Possible voice automation using google home to interact with system
    Deep sleep settings that will wake on touch to tablet
        Maybe even motion sensed
    Investigate camera for tablet
    Investigate switch over to raspberry pi interface
    Security camera support
    Battery gauge for tablet
    Learn how to use threads to send out threads to gather information and update tablet on system information
    Investigate root issues on tablet
    Create list of kernel/system settings that may need to be tweaked on tablet
    Get wifi/ethernet information - ip address
    Maybe a netscan interface to check overall network health and connected devices
    Keep searching for ability to use pi compute module and touch screen
'''


from apps import *
from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, NoTransition
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')


class MainApp(App):
    sm = ScreenManager()
    sm.id = "manager"
    sm.transition = NoTransition()

    def test(self):
        print("TEST")

    def add_app(self, app_name):
        print(app_name)

    def build(self):
        self.sm.add_widget(HomeScreen())
        return self.sm


if __name__ == "__main__":
    app = MainApp().run()