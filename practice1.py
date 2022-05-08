


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
matplotlib.style.use('ggplot')

mtcars = pd.read_csv("data.csv")



# x = mtcars.Area.values
# y = mtcars.rooms.values


# m = (np.mean(x*y)-np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x) ** 2)
# b = np.mean(y) - m * np.mean(x)
# print(m, b)

# plt.scatter(x, y, color = "m", marker = "o", s = 10)
# plt.plot(b, 'b')
# plt.xlabel('Area')
# plt.ylabel('Number of rooms')
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
 
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
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, pred, color = "g")
 
    # putting labels
    plt.xlabel('Area')
    plt.ylabel('Number of rooms')
 
    # function to show plot
    plt.show()
 
def main():
    # observations / data
    x = mtcars.Area.values
    y = mtcars.rooms.values
 
    # estimating coefficients
    b = calculating_m_b(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()