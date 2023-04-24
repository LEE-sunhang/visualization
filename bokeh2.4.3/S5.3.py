from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup
from bokeh.models.annotations import LabelSet
from bokeh.layouts import layout

# Create the figure
x_range = ["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
y_range = ["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
f = figure(height=450,
           width=450,
           x_range=x_range,
           y_range=y_range)


# Create CDS with a given grade_dict
grades_dict = dict(average_grades=["B+", "A", "D-"],
                   exam_grades=["A+", "C", "D"],
                   student_names=["Stephan", "Helder", "Riazudidn"])
grades = ColumnDataSource(grades_dict)


# Add multiple description labels via LabelSet
labels = LabelSet(x='average_grades',
                  y='exam_grades',
                  text='student_names',
                  x_offset=5, y_offset=5,
                  source=grades)
f.add_layout(labels)
curdoc().add_root(f)


# Add glyphs
f.circle(x='average_grades',
         y='exam_grades',
         size=8,
         source=grades)

# Create RadioButtonGroup widgets
options = ['average_grades', 'exam_grades', 'student_names']
radio_button_group = RadioButtonGroup(labels=options)

# Create a funciton that updates the description via LabelSet.text
def update_descriotion(attr, old, new):
    
    # RadioButtonGroup.active creates
    # Check JSON Prototype via https://docs.bokeh.org/en/2.4.3/docs/reference/models/widgets/groups.html#bokeh.models.ButtonGroup
    
    # RadioButtonGroup.active returns the index of the selected radio box, or None if nothing is selected
    labels.text = options[radio_button_group.active]
    
radio_button_group.on_change('active', update_descriotion)

# Create layout and add to curdoc
lay_out = layout( [[radio_button_group]] )
curdoc().add_root(lay_out)