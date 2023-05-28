import numpy as np
import matplotlib.pyplot as plt

# create data for sin curve and cos curve
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin") # plot sin curve
plt.plot(x, y2, linestyle="--", label="cos")  # plot cos curve
plt.xlabel("x") # x axis label
plt.ylabel("y") # y axis label
plt.title('sin & cos') # title
plt.legend()
plt.show()
