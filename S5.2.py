from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.annotations import LabelSet
from bokeh.models.widgets import Select
from bokeh.layouts import layout


# Create a ColumnData Srouce object (or CDS) 
grades_dict = dict(average_grades=["B+", "A", "D-"],
                   exam_grades=["A+", "C", "D"],
                   student_names=["Stephan", "Helder", "Riazudidn"])

source = ColumnDataSource(grades_dict)


# Create the figure
x_range = ["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
y_range = ["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
f = figure(height=450,
           width=450,
           x_range=x_range,
           y_range=y_range)


# Add labels for glyphs
labels = LabelSet(x='average_grades',
                  y='exam_grades',
                  text='student_names',
                  x_offset=5,
                  y_offset=5,
                  source=source)
f.add_layout(labels)


# Create a function for widget
def update_labels(attr, old, new):
    labels.text = select.value

# Create select widget
# options = [("column_name", "dropdown name"),...]
options = [("average_grades", "Average Grades"),
           ("exam_grades", "Exam Grades"),
           ("student_names", "Student Names")]
select = Select(title="Attribute", options=options, size=8)

select.on_change("value", update_labels)


# Create layout and add to curdoc
lay_out = layout( [select] )
curdoc().add_root(f)
curdoc().add_root(lay_out)



# Create glyphs
f.circle(x='average_grades',
         y='exam_grades',
         size=8,
         source=source)




# Need bokeh server to utilize widgets
# To open multiple servers: python -m bokeh serve S5.2.py --port 5007 (if 5006 already exists)