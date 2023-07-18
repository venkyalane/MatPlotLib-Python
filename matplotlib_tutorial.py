# install matplotlib library (pip install matplotlib)

import matplotlib
# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([100,200])
ypoints = np.array([50,100])

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
plt.plot(xpoints,ypoints)

# Plotting Without Line
plt.plot(xpoints,ypoints, 'o')

#plt.scatter(xpoints,ypoints)
plt.show()


# Multiple Points
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
# If we do not specify the points on the x-axis,
# they will get the default values 0, 1, 2, 3 (etc., depending on the length of the y-points.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


# Markers
# You can use the keyword argument marker to emphasize each point with a specified marker:
import matplotlib.pyplot as plt
import numpy as np

# Markers => o,*,.,
# ms = marker size
# mec = marker color
# mfc = marker face color
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints, marker='*', ms= 20, mec = 'r', mfc = '#4CAF50')
plt.show()


# Format string
import matplotlib.pyplot as plt
import numpy as np

# str => :(dotted line), -.(das and dotted line), --(dashed line), -(plain line)
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints, 'o-.b')
#o = marker format
#r = color format
plt.show()


# Lines
# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1 = np.array([5, 7, 3, 9])
y2 = np.array([6, 2, 7, 11])

#plt.plot(ypoints, ls='-.', color = 'r')
# linestyle / ls = 'dotted' / ':', 'dashed' / '--', 'dashdot' / '-.'
#plt.plot(ypoints, color = 'r')
plt.plot(ypoints, linewidth = '5')
plt.plot(y1, color = 'r')
plt.plot(y2, color = 'pink')
plt.show()

# adding multiple lines in one plot function
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)

plt.show()



# Create Lable and Title for Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 130])
y = np.array([50, 100, 50, 100, 50, 150, 250, 350, 250, 50])

# Set Font Properties for Title and Labels
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# Create Labels for a Plot
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
plt.xlabel("Average Pulse", fontdict=font2)       # create lable for x plot
plt.ylabel("Calorie Burnage", fontdict=font2)     # create lable for y plot

# Position the Title
# You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
plt.title("Sports watch data", fontdict=font1, loc='left')    # create title for plot


plt.scatter(x, y)
plt.plot(x, y)

plt.show()

# Add Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot.
# plt.grid()

# Specify Which Grid Lines to Display
# You can use the axis parameter in the grid() function to specify which grid lines to display.
# Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
# plt.grid(axis='x')
# plt.grid(axis= 'y')

# Set Line Properties for the Grid
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 130])
y = np.array([50, 100, 50, 100, 50, 150, 250, 350, 250, 50])


font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports watch data", fontdict=font1, loc='left')    # create title for plot
plt.xlabel("Average Pulse", fontdict=font2)       # create lable for x plot
plt.ylabel("Calorie Burnage", fontdict=font2)     # create lable for y plot

#plt.scatter(x, y)
plt.plot(x, y)
plt.grid(axis='x', color='r', linestyle='--')
plt.grid(axis='y', color='b', linestyle='--')

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
y = np.array([25, 50, 100, 175, 250, 325, 400, 500])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Employee Joining Data", fontdict=font1)
plt.xlabel("Year", font2)
plt.ylabel("Joined Employee", font2)

plt.plot(x, y)
plt.grid(axis='y', ls='--', color='r')
plt.grid(axis='x', ls='--', color='g')
plt.show()


# Matplotlib Subplot (Display Multiple Plots)
# With the subplot() function you can draw multiple plots in one figure:
# subplot() function take 3 arguments,first two arguments is row and column and third argument is plot number.
# plt.title() function asign a title name of every plot
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

#the figure has 1 row, 3 columns, and this plot is the first plot.
plt.subplot(1, 3, 1)
plt.plot(x,y)
plt.title("First Plot")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

#the figure has 1 row, 3 columns, and this plot is the second plot.
plt.subplot(1, 3, 2)
plt.plot(x,y)
plt.title("Second Plot")

#plot 3:
x = np.array([0,1,2,3])
y = np.array([100,200,300,400])

#the figure has 1 row, 3 columns, and this plot is the third plot.
plt.subplot(1,3,3)
plt.plot(x,y)
plt.title("Third Plot")

plt.suptitle("Main Plot")
plt.show()


# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.
# The scatter() function plots one dot for each observation. It needs two arrays of the same length,
# one for the values of the x-axis, and one for values on the y-axis:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.show()

# Compare Plots
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color="hotpink")

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color="#88c999")

plt.title("Compare Plot")
plt.show()

# Color Each Dot
# You can even set a specific color for each dot by using an array of colors as value for the c argument:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)
plt.title("Plot with different color points")
plt.show()

# ColorMap
# The Matplotlib module has a number of available colormaps.
# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
# c_map = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 
#          'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 
#          'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 
#          'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 
#          'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 
#          'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 
#          'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 
#          'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 
#          'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 
#          'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 
#          'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 
#          'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 
#          'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 
#          'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 
#          'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 
#          'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])

plt.scatter(x, y, c=colors, cmap='bone')
plt.title("Plot using ColorMap")
plt.colorbar()
plt.show()


# Size
# You can change the size of the dots with the s argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors ,s=sizes, cmap='YlGnBu_r')
plt.title("change the size of dots and different colors")
plt.show()


# Alpha (range= 0 to 1)
# You can adjust the transparency of the dots with the alpha argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.subplot(2,2,1)
plt.scatter(x, y, s=sizes, alpha=0.1)
plt.title("transparency: 0.1")

plt.subplot(2,2,2)
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title("transparency: 0.5")

plt.subplot(2,2,3)
plt.scatter(x, y, s=sizes, alpha=0.7)
plt.title("transparency: 0.7")

plt.subplot(2,2,4)
plt.scatter(x, y, s=sizes, alpha=1.0)
plt.title("transparency: 1.0")
plt.show()


# Combine Color Size and Alpha
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.title("combine colors,size and alpha")
plt.colorbar()

plt.show()


# Creating Bars(Vertical)
# With Pyplot, you can use the bar() function to draw bar graphs:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([10,20,10,15])

plt.subplot(1,2,1)
plt.bar(x, y, color='red', width=0.5)
plt.title("Vertical bar width:0.5")

plt.subplot(1,2,2)
plt.barh(x, y, color='green', height=0.5)
plt.title("horizontal bar height:0.5")

plt.suptitle("creating bars")
plt.show()


# Matplotlib Pie Charts (Creating Pie Charts)
# With Pyplot, you can use the pie() function to draw pie charts:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 15,10])
mylables = ['Nanded', 'Pune', 'Aurangabad', 'Mumbai', 'Latur']
myexplode = [0.2, 0.2, 0.2, 0.2, 0.2]

plt.subplot(2,2,1)
plt.pie(x, shadow=True)
plt.title("Pie chart")

plt.subplot(2,2,2)
plt.pie(x, labels=mylables, shadow=True)
plt.title("Pie chart with lables")

plt.subplot(2,2,3)
plt.pie(x, labels=mylables, explode=myexplode)
plt.title("Pie chart with lables and explode")

plt.subplot(2,2,4)
plt.pie(x, labels=mylables)
plt.legend(title='Five Cities')
plt.title("Pie chart with legend")

plt.suptitle("Pie chrats")
plt.show()

