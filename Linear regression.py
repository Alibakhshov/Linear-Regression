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
        self.linReg_window = GridLayout()
        self.linReg_window.cols = 1
        self.linReg_window.size_hint = (0.6, 0.7)
        self.linReg_window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        
        
        # image widget
        self.linReg_window.add_widget(Image(source="./Images/UCA.png"))
        
        # Label widget
        self.lin_reg = Label(  
                              text="Linear Regression",
                              font_size = 30,
                              color = '#00FFCE',
                              size_hint = (1, 0.5)
                              )
        self.linReg_window.add_widget(self.lin_reg)
        
        self.m = Label(  
                              text="",
                              font_size = 30,
                              color = '#00FFCE',
                              size_hint = (1, 0.5),
                              padding = (2, 5),
                              pos_hint = {"center_x": 50, "center_y":0.5}
                              )
        self.linReg_window.add_widget(self.m)
        
        # Text input widget
        self.m_out = TextInput(
                            #   multiline=False,
                              padding_y = (20, 10),
                              size_hint = (1, 0.5)
                              )
        self.linReg_window.add_widget(self.m_out)
        
        self.b_out = TextInput(
                            #   multiline=False,
                              padding_y = (20, 10),
                              size_hint = (1, 0.5)
                              )
        self.linReg_window.add_widget(self.b_out)
        
        # button widget
        self.calculate = Button(
                              text="Calculate",
                              size_hint = (1, 0.5),
                              bold = True,
                              background_color = '#00FFCE'                     
                              )
        self.linReg_window.add_widget(self.calculate)
        self.calculate.bind(on_press=self.LinearRegressionCalculate)
        
        self.exitButton = Button(
                              text="Exit",
                              size_hint = (1, 0.5),
                              bold = True,
                              background_color = '#00FFCE'                     
                              )
        self.linReg_window.add_widget(self.exitButton)
        self.exitButton.bind(on_press=self.close)
        
        return self.linReg_window

        
    def LinearRegressionCalculate(self, instance):
        global m, b
        
        data = pd.read_csv("data.csv")
        def calculating_m_b(x, y):
            n = np.size(x)
            x_mean = np.mean(x)
            y_mean = np.mean(y)
            deviation_xy = np.sum(y*x) - n*y_mean*x_mean
            deviation_xx = np.sum(x*x) - n*x_mean*x_mean
            m = deviation_xy / deviation_xx
            b = y_mean - m*x_mean
            return (b, m)
        
        def main():
            x = data.Area.values
            y = data.rooms.values
            b = calculating_m_b(x, y)
            self.m_out.text = str(b[0])
            self.b_out.text = str(b[1])
            plotting_graph(x, y, b)
        
        def plotting_graph(x, y, b):
            plt.scatter(x, y, color = "m", marker = "o", s = 30)
            pred = b[0] + b[1]*x
            plt.plot(x, pred, color = "g")
            plt.xlabel('Area')
            plt.ylabel('Number of rooms')
            plt.show()
        
        
        
        if __name__ == "__main__":
            main()
        
        
  
  
    def close(self):
        self.linReg_window.close()  
    

        

if __name__ == "__main__":
    LinearRegression().run()