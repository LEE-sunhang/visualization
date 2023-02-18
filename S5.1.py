from bokeh.io import curdoc # current doc that will be displayed in the browser
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# Create widgets
text_input = TextInput(value='Sun')
button = Button(label='Generate Text')
output = Paragraph() # Paragrah only works in Bokeh server


def update():
    output.text = f"Hello, {text_input.value}"
    
button.on_click(update)

lay_out = layout([[button, text_input],[output]])

curdoc().add_root(lay_out)


# Command: python -m bokeh serve S5.1.py