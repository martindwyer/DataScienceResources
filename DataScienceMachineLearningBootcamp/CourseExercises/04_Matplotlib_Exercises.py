import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

"""
Exercise 1

** Follow along with these steps: **

** Create a figure object called fig using plt.figure() **
** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

"""

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,z)
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('title')

plt.show()

"""

Exercise 2
** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

"""

fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')


ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')


plt.show()

"""
Exercise 3
** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
"""

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])

ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')


ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.show()

"""
Exercise 4
** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**
"""

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')

plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')

plt.show()

