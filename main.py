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


from sys import exit
from os import listdir
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.slider import Slider
from kivy.uix.button import Button, Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class HomeScreen(Screen):
    # TODO: Investigate login screen with virtual keypad
    # TODO: Investigate Virtual keyboard
    # TODO: Investigate battery gauge for tablet
        # Exit i3 and get back to main armbian screen -
        # look at start up script to find where it gets battery information
    # TODO: Find more things to add to homescreen

    def add_app(self):
        # TODO: Find a way to dynamically add homescreen buttons/apps
        pass

    def delete_app(self):
        # TODO: Find a way to dynamically delete homescreen buttons/apps
        pass

    def close_gui(self):
        exit()


class MusicScreen(Screen):
    pass


class LightScreen(Screen):

    # TODO: Add functionality to get real time updates on light states
    # TODO: Add functionality to drop down options for lights
    # TODO: Add slider functionality for dimmable lights
    # TODO: Make some kind of built in system to categorize types of lights
        # Dimmable, rgb, outlets, fans, etc

    def add_light(self):
        # TODO: Add functionality to add light buttons
        pass

    def delete_light(self):
        # TODO: Add functionality to delete light buttons
        pass

    def update_light_states(self):
        # TODO: Add functionality to update light states around the house
        pass


class SettingScreen(Screen):
    oldval = 0

    # TODO: Find more settings that would be good to access on tablet
        # Wifi / ethernet settings
        # login information
    def update_backlight_val(self, value):
        if self.oldval != value:
            self.oldval = value
            print(int(value))

            # TODO: Add in functionality to edit backlight value on tablet


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.transition = NoTransition()
        sm.add_widget(HomeScreen(name='Home'))
        sm.add_widget(LightScreen(name='Lights'))
        sm.add_widget(SettingScreen(name='Settings'))

        return sm


if __name__ == "__main__":
    app = MainApp().run()
