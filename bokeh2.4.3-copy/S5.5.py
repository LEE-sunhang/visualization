import numpy as np
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Select, Slider
from bokeh.models.annotations import LabelSet
from bokeh.layouts import layout

# Dataset
grades_dict = dict(average_grades=[7,8,10],
                   exam_grades=[6,8,9],
                   student_names=['Stephan', 'Helder', 'Riazudidn'])

# Create CDS
source = ColumnDataSource(grades_dict)
source_original = ColumnDataSource(grades_dict)

# Create the figure
f = figure(x_range=Range1d(start=0, end=12),
           y_range=Range1d(start=0, end=12))


# Add glyphs
f.circle(x='average_grades',
         y='exam_grades',
         size=8,
         source=source)


# Add multiple description labels via LabelSet
labels = LabelSet(x='average_grades',
                  y='exam_grades',
                  text='student',
                  x_offset=5, y_offset=5,
                  source=source)
f.add_layout(labels)

# Add f to curdoc() via add_root
curdoc().add_root(f)


# Create Select widget
options = [('average_grades', 'Average Grades'),
           ('exam_grades', 'Exam Grades'),
           ('student_names', 'Student Names')]
select = Select(title='Attribute', options=options)

# Create a function that updates label descriptions
def update_labels(attr, old, new):
    labels.text = select.value

select.on_change('value', update_labels)


# Create Slider widget
start_slider = np.array(source.data['exam_grades']).min() - 1
end_slider = np.array(source.data['exam_grades']).max() + 1
slider = Slider(start=start_slider,
                end=end_slider,
                value=8,
                step=0.1,
                title='Exam Grade: ')

# Create a function that filters values for slider
# IMPORTANT! 중요 알고리즘! 
def update_slider(attr, old, new):
    """
    1. Must maintain source_original as a benchmark reference object
    2. When slider toggle changes value by on_change method, this change must reflect in source object 
        a. many other objects (eg. glyphs, select, etc) depend on source, not source_original
        b. loop through source_original as the main reference
    """
    
    # source.data={key:[value for i, value in enumerate(source_original.data[key]) if source_original.data["exam_grades"][i]>=slider.value] for key in source_original.data}
    # print(slider.value)
    
    source_dict = dict()
    for key in source_original.data:
        
        value_list = []
        for idx, value in enumerate(source_original.data[key]):
            if source_original.data['exam_grades'][idx] >= slider.value:
                value_list.append(value)
                
        source_dict[key] = value_list
    
    source.data = source_dict
    print(slider.value)
    
slider.on_change('value', update_slider)

lay_out = layout( [[select],[slider]] )
curdoc().add_root(lay_out)