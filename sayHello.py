from glob import glob
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pyrsistent import b

from sympy.functions import sin,cos
import matplotlib.pyplot as plt
from sympy.functions import sin,cos
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearRegression(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window
        
        # image widget
        self.window.add_widget(Image(source="./Images/UCA.png"))
        
        # Label widget
        self.lin_reg = Label(  
                              text="Linear Regression",
                              font_size = 30,
                              color = '#00FFCE',
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.lin_reg)
        
        self.m = Label(  
                              text="m",
                              font_size = 30,
                              color = '#00FFCE',
                              size_hint = (1, 0.5),
                              padding = (2, 5),
                              pos_hint = {"center_x": 5, "center_y":0.5}
                              )
        self.window.add_widget(self.m)
        
        # Text input widget
        self.user = TextInput(
                            #   multiline=False,
                              padding_y = (20, 20),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.user)
        
        # .input_filter='int'
        
        self.user1 = TextInput(
                            #   multiline=False,
                              padding_y = (20, 20),
                              size_hint = (1, 0.5)
                              )
        self.window.add_widget(self.user1)
        
        # button widget
        self.calculate = Button(
                              text="Calculate",
                              size_hint = (1, 0.5),
                              bold = True,
                              background_color = '#00FFCE'                     
                              )
        self.window.add_widget(self.calculate)
        self.calculate.bind(on_press=self.callback)
        
        self.exitButton = Button(
                              text="Exit",
                              size_hint = (1, 0.5),
                              bold = True,
                              background_color = '#00FFCE'                     
                              )
        self.window.add_widget(self.exitButton)
        self.exitButton.bind(on_press=self.close)
        
        
        
        
        return self.window

        
    def callback(self, instance):
        # self.greeting.text = "Hello " + self.user.text + "!"
        # self.greeting.text = str(int(self.user.text)  + int(self.user1.text))
        global m, b
        
        mtcars = pd.read_csv("data.csv")
        def calculating_m_b(x, y):
            # number of observations/points
            n = np.size(x)
        
            # mean of x and y vector
            x_mean = np.mean(x)
            y_mean = np.mean(y)
        
            # calculating cross-deviation and deviation about x
            deviation_xy = np.sum(y*x) - n*y_mean*x_mean
            deviation_xx = np.sum(x*x) - n*x_mean*x_mean
        
            # calculating regression coefficients
            m = deviation_xy / deviation_xx
            b = y_mean - m*x_mean
        
            return (b, m)
        
        def main():
            # observations / data
            x = mtcars.Area.values
            y = mtcars.rooms.values
        
            # estimating coefficients
            b = calculating_m_b(x, y)
            self.user.text = str(b[0])
            self.user1.text = str(b[1])
            
            # print("Estimated coefficients:\nm = {}  \
            #     \nb = {}".format(b[0], b[1]))
        
            # plotting regression line
            plotting_graph(x, y, b)
        
        def plotting_graph(x, y, b):
            # plotting the actual points as scatter plot
            plt.scatter(x, y, color = "m", marker = "o", s = 30)
        
            # predicted response vector
            pred = b[0] + b[1]*x
        
            # plotting the regression line
            plt.plot(x, pred, color = "g")
        
            # putting labels
            plt.xlabel('Area')
            plt.ylabel('Number of rooms')
        
            # function to show plot
            plt.show()
        
        
        
        if __name__ == "__main__":
            main()
        
        
  
  
    def close(self):
        self.window.close()  
    

        

if __name__ == "__main__":
    LinearRegression().run()