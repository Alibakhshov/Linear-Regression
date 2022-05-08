


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
matplotlib.style.use('ggplot')

mtcars = pd.read_csv("data.csv")



x = mtcars.Area.values
y = mtcars.rooms.values


m = (np.mean(x*y)-np.mean(x) * np.mean(y)) / (np.mean(x**2) - np.mean(x) ** 2)
b = np.mean(y) - m * np.mean(x)
print(m, b)

plt.scatter(x, y, color = "m", marker = "o", s = 10)
plt.plot(x, y, 'b')
plt.xlabel('Area')
plt.ylabel('Number of rooms')
plt.show()