#Plotting flower species

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("S3.9-iris.html")

#Create the figure object
f = figure()

#Style the tools
f.tools = [PanTool(),ResetTool()]
f.add_tools(HoverTool())
f.toolbar_location = 'above'
f.toolbar.logo = None

#Style the plot area
f.width = 1100
f.height = 650
f.background_fill_color = "olive"
f.background_fill_alpha = 0.3

#Style the title
f.title.text = "Iris Morphology"
f.title.text_color = "olive"
f.title.text_font = "Agency FB"
f.title.text_font_size = "25px"
f.title.align = "center"

#Style the axes
f.xaxis.minor_tick_line_color = "blue"
f.yaxis.major_label_orientation = "vertical"
f.xaxis.visible = True
f.xaxis.minor_tick_in = -6
f.xaxis.axis_label = "Petal Length"
f.yaxis.axis_label = "Petal Width"
f.axis.axis_label_text_color = "blue"
f.axis.major_label_text_color = "orange"

#Axes geometry
f.x_range = Range1d(start=0, end=10)
f.y_range = Range1d(start=0, end=5)
f.xaxis.bounds = (2,6)
f.xaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.num_minor_ticks = 10

#Style the grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha = 0.6
f.grid.grid_line_dash = [5,3]

colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
flowers['color']=[colormap[x] for x in flowers['species']]

#adding glyphs
f.circle(x=flowers["petal_length"], y=flowers["petal_width"],
         size=flowers['sepal_width']*4, fill_alpha=0.2, color=flowers['color'], line_dash=[5,3])
#Warning!# 
#line_dash produces Error - deprecation# 

#Save and show the figure
show(f)
