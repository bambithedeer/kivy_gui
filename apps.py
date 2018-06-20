from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from layouts import *


class HomeScreen(Screen):

    # TODO: Investigate login screen with virtual keypad
    # TODO: Investigate Virtual keyboard
    # TODO: Investigate battery gauge for tablet
    # Exit i3 and get back to main armbian screen -
    # look at start up script to find where it gets battery information
    # TODO: Find more things to add to homescreen

    def delete_but(self):

        # TODO: Find a way to dynamically add homescreen buttons/apps

        print(str(self.parent.numButtons) + " " + str(self.parent.minButtons))

        if self.parent.numButtons - 1 >= self.parent.minButtons:
            self.parent.numButtons = self.parent.numButtons - 1
            print(self.parent.numButtons)
            return self.parent.numButtons
        else:
            print("Not enough space to add a new app!")
            return self.parent.numButtons

    def add_but(self):

        # TODO: Find a way to dynamically add homescreen buttons/apps

        print(str(self.parent.numButtons) + " " + str(self.parent.maxButtons))

        if self.parent.numButtons + 1 <= self.parent.maxButtons:
            self.parent.numButtons = self.parent.numButtons + 1
            ## self.parent.add_widget(Button(text="ADDED", id="test"))
            print(self.parent.numButtons)
            return self.parent.numButtons
        else:
            print("Not enough space to add a new app!")
            return self.parent.numButtons

    def close_gui(self):
        exit()

    grid = HomeGrid()
    grid.add_widget(Button(id="add", text="Add", on_press=add_but))
    grid.add_widget(Button(id="delete", text="Delete", on_press=delete_but))
    grid.add_widget(Button(id="quit", text="Quit", on_press=close_gui))

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.add_widget(self.grid)


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

