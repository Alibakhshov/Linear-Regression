from distutils.command.build import build
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
matplotlib.style.use('ggplot')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'
            on_press: root.manager.current = 'close'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'close window'
            on_press: root.manager.current = 'button'
        
<closeScreen>:
    GridLayout:
        Button:
            on_press: root.text(txt_inpt.text)
        TextInput:
            id: txt_inpt


        Button:
            on_press: root.text(txt_inpt.text)
        TextInput:
            id: txt_inpt

""")

global button

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class closeScreen(Screen):
    pass
    mtcars = pd.read_csv("data.csv")
    x = mtcars.Area.values
    y = mtcars.rooms.values


    m = (np.mean(x*y)-np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x) ** 2)
    b = np.mean(y) - m * np.mean(x)
    print(m, b)

    plt.scatter(x, y, color = "m", marker = "o", s = 10)
    plt.plot(b, 'b')
    plt.xlabel('Area')
    plt.ylabel('Number of rooms')
    plt.show()
    
    
class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SettingsScreen(name='close'))
        sm.add_widget(closeScreen(name='button'))
        
        
        return sm


if __name__ == '__main__':
    TestApp().run()