import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.io import curdoc, show, output_file
from bokeh.sampledata.periodic_table import elements
from bokeh.models import ColumnDataSource, Span, BoxAnnotation
from bokeh.models.widgets import Select
from bokeh.layouts import layout


# Remove NaN rows then map color by 'standard state'
elements.dropna(inplace=True)
colormap_dict = {'gas':'yellow',
                 'liquid':'orange',
                 'solid':'red',
                 np.nan: 'gray'}

# Create color and size columns for glyphs
elements['color'] = elements['standard state'].apply(lambda x: colormap_dict[x])
elements['size'] = elements['van der Waals radius'] / 10

# Create each DataFrame with query method via 'standard state' column
df_gas = elements.query("`standard state` == 'gas'", engine='python')
df_liquid = elements.query("`standard state` == 'liquid'", engine='python')
df_solid = elements.query("`standard state` == 'solid'", engine='python')

# Created CDS
gas = ColumnDataSource(df_gas)
liquid = ColumnDataSource(df_liquid)
solid = ColumnDataSource(df_solid)


# Create the figure object
f = figure()

# Add glyphs
f.circle(x='atomic radius',
         y='boiling point',
         size='size',
         color='color',
         fill_alpha=0.2,
         legend_label='Gas',
         source=gas)
f.circle(x='atomic radius',
         y='boiling point',
         size='size',
         color='color',
         fill_alpha=0.2,
         legend_label='Liquid',
         source=liquid)
f.circle(x='atomic radius',
         y='boiling point',
         size='size',
         color='color',
         fill_alpha=0.2,
         legend_label='Solid',
         source=solid)

# Style the axis
x, y, z = f.xaxis, f.yaxis, f.axis
x.axis_label = 'Atomic radius'
y.axis_label = 'Boiling point'

# Add figure to curdoc() via add_root() method
curdoc().add_root(f)


"""
IMPORTANT! the options attribute in Select widgets expects value as...
    1. List[Tuple(String, String)] 
    2. or Dict[key:List(Strings...)]
"""
# options = [( str(solid.data['boiling point'].mean()), 'Average Boiling Point'), 
#            ( str(solid.data['boiling point'].min()), 'Minimum Boiling Point'),
#            ( str(solid.data['boiling point'].max()), 'Maximum Boiling Point')]
# select = Select(title='Dropdowns', options=options)
options = {'Maximum Boiling Point': [str(solid.data['boiling point'].max()), str(liquid.data['boiling point'].max()), str(gas.data['boiling point'].max())],
           'Average Boiling Point': [str(solid.data['boiling point'].mean()), str(liquid.data['boiling point'].mean()), str(gas.data['boiling point'].mean())],
           'Minimum Boiling Point': [str(solid.data['boiling point'].min()), str(liquid.data['boiling point'].min()), str(gas.data['boiling point'].min())]}
# Create Select widget with options attribute
select = Select(title='Dropdowns', options=options)


# Create a function that updates the Span location via Select.value 
def update_span(attr, old, new):
    
    # Create a Span
    span = Span(dimension='width',
                line_width=2)
    
    # IMPORTANT! Select.value returns String thus need to convert to float
    span.location = float(select.value) # select.value: str
    
    # Add different Span color via solid, liquid, gas boiling point range
    if solid.data['boiling point'].min() <= float(select.value) and float(select.value) <= solid.data['boiling point'].max():
        span.line_color = 'red'
        
    if liquid.data['boiling point'].min() <= float(select.value) and float(select.value) <= liquid.data['boiling point'].max():
        span.line_color = 'orange'
        
    if gas.data['boiling point'].min() <= float(select.value) and float(select.value) <= gas.data['boiling point'].max():
        span.line_color = 'yellow'
        
    # Add Span to the figure via add_layout method
    f.add_layout(span)


# Add a callback on Select object to trigger when attr changes.
# IMPORTANT! need to add "value"
select.on_change("value", update_span)


# Add Select widget to layout 
lay_out = layout( [[select]] )
# To curdoc
curdoc().add_root(lay_out)