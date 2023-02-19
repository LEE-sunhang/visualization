from bokeh.io import curdoc 
# current doc that will be displayed in the browser

from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# Create widgets
text_input = TextInput(value='Sun')
button = Button(label='Click here')
output = Paragraph()

def update():
    output.text = f"Hello, {text_input.value}"
    
button.on_click(update)

lay_out = layout(children= [[button, text_input],
                            [output]],
                 sizing_mode='stretch_both')

curdoc().add_root(lay_out)
# Command: python -m bokeh serve S5.1.py