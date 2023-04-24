# Widgets - TextInput, Button, Paragraph

from bokeh.io import output_file, show
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout


# Define the bokeh output
output_file("S5.0-simple_bokeh.html")

# Create widgets
text_input = TextInput(value='Sun')
button = Button(label='Generate Text')
output = Paragraph() # Paragrah only works in Bokeh server


def update():
    output.text = f"Hello {text_input.value}"
    
button.on_click(update)

lay_out = layout([[button, text_input],[output]])

show(lay_out)