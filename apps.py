from kivy.uix.screenmanager import Screen
from layouts import *


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        HomeGrid.rows = 4
        HomeGrid.cols = 4
        HomeGrid.maxButtons = 16
        HomeGrid.minButtons = 3
        HomeGrid.numButtons = 3


    # TODO: Investigate login screen with virtual keypad
    # TODO: Investigate Virtual keyboard
    # TODO: Investigate battery gauge for tablet
        # Exit i3 and get back to main armbian screen -
        # look at start up script to find where it gets battery information
    # TODO: Find more things to add to homescreen

    def add_but(self, num_but, max_but):
        # TODO: Find a way to dynamically add homescreen buttons/apps

        print(str(num_but) + " " + str(max_but))

        if num_but + 1 <= max_but:
            num_but = num_but + 1
            print(num_but)
            return num_but
        else:
            print("Not enough space to add a new app!")
            return num_but

    def delete_but(self, num_but, min_but):
        # TODO: Find a way to dynamically delete homescreen buttons/apps
        print(str(num_but) + " " + str(min_but))
        if num_but - 1 >= min_but:
            num_but = num_but - 1
            print(num_but)
            return num_but
        else:
            print("No more apps to delete!")
            return num_but

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

