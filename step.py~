import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import FileOpen as fo

mpl.use('tkAgg')
fig,ax= plt.subplots(figsize=(6,6))


j = 1.0 * 10**-19
omega= 1.9 * 2.0* np.pi * 10 **12
a = [0] * 1001

def step():
    for c in range(-200,800):
        if c<=0:
            a[c + 201] = 0
        else:
            a[c + 201] = 1 
    return a

tate = step()

t = np.linspace(-2, 8, 1001)

ax.plot(t,tate, "o")
plt.show()
