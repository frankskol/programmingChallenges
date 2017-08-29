import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
import random
import math

rnumber = random.randint(0, 100)
X = np.linspace(rnumber - 10, rnumber + 10 , 360, endpoint = True)
Y = np.sin(X)
plt.xlabel('Number generated: ' + str(rnumber))
plt.ylabel('Sinus for Number')
plt = pl.gcf()
plt.canvas.set_window_title('Random Number Sinus Plotter')
pl.plot(rnumber, math.sin(rnumber), 'o')
pl.plot (X, Y)
pl.show()