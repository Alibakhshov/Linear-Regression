from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from sympy.functions import sin,cos
import matplotlib.pyplot as plt
from sympy.functions import sin,cos
import matplotlib.pyplot as plt
import numpy as np

class LinearRegression(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window
        
        # image widget
        self.window.add_widget(Image(source="./Images/1.png"))
        
        # Label widget
        self.greeting = Label(  
                              text="What's your name",
                              font_size = 18,
                              color = '#00FFCE'
                              )
        self.window.add_widget(self.greeting)
        
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
        self.button = Button(
                              text="Greet",
                              size_hint = (1, 0.5),
                              bold = True,
                              background_color = '#00FFCE'                     
                              )
        self.window.add_widget(self.button)
        self.button.bind(on_press=self.callback)
        
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
  
        def estimate_coef(x, y):
            # number of observations/points
            n = np.size(x)
        
            # mean of x and y vector
            m_x = np.mean(x)
            m_y = np.mean(y)
        
            # calculating cross-deviation and deviation about x
            SS_xy = np.sum(y*x) - n*m_y*m_x
            SS_xx = np.sum(x*x) - n*m_x*m_x
        
            # calculating regression coefficients
            b_1 = SS_xy / SS_xx
            b_0 = m_y - b_1*m_x
        
            return (b_0, b_1)
        
        def plot_regression_line(x, y, b):
            # plotting the actual points as scatter plot
            plt.scatter(x, y, color = "m",
                    marker = "o", s = 30)
        
            # predicted response vector
            y_pred = b[0] + b[1]*x
        
            # plotting the regression line
            plt.plot(x, y_pred, color = "g")
        
            # putting labels
            plt.xlabel('x')
            plt.ylabel('y')
        
            # function to show plot
            plt.show()
        
        def main():
            # observations / data
            x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
        
            # estimating coefficients
            b = estimate_coef(x, y)
            print("Estimated coefficients:\nb_0 = {}  \
                \nb_1 = {}".format(b[0], b[1]))
        
            # plotting regression line
            plot_regression_line(x, y, b)
        
        if __name__ == "__main__":
            main()
        
    def close(self):
        self.window.close()  
        

if __name__ == "__main__":
    LinearRegression().run()