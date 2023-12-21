import panel as pn
from flask import Flask, render_template
from bokeh.embed import server_document
from tornado.ioloop import IOLoop

app = Flask(__name__)
from utils import *

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Instantiate the ChatBot class
cb = cbfs()


# Create the dashboard
jpg_pane = pn.pane.Image('./img/convchain.jpg')
file_input = pn.widgets.FileInput(accept='.pdf')
button_load = pn.widgets.Button(name="Load DB", button_type='primary')
button_clearhistory = pn.widgets.Button(name="Clear History", button_type='warning')
button_clearhistory.on_click(cb.clr_history)
button_clearhistory2 = pn.widgets.Button(name="Clear Panel", button_type='warning')
button_clearhistory2.on_click(cb.clr_panels)

inp = pn.widgets.TextInput(placeholder='Enter text here…')

bound_button_load = pn.bind(cb.call_load_db, button_load.param.clicks)
conversation = pn.bind(cb.convchain, inp)

tab1 = pn.Column(
    pn.Row(inp),
    pn.layout.Divider(),
    pn.panel(conversation, loading_indicator=True, height=700),
    pn.layout.Divider(),
)
tab2 = pn.Column(
    pn.panel(cb.get_lquest),
    pn.layout.Divider(),
    pn.panel(cb.get_sources),
)
tab3 = pn.Column(
    pn.panel(cb.get_chats),

)
tab4 = pn.Column(
    pn.Row(file_input, button_load, bound_button_load),
    pn.Row(button_clearhistory, pn.pane.Markdown("Clears chat history. Can use to start a new topic")),
    pn.Row(button_clearhistory2,  pn.pane.Markdown("Clears chat history in the chatbot interface")),

    pn.Row(jpg_pane.clone(width=400))
)
dashboard_content = pn.Column(
    pn.Row(pn.pane.Markdown('# ChatWithYourData_Bot')),
    pn.Tabs(('Conversation', tab1), ('Database', tab2), ('Chat History', tab3), ('Configure', tab4))
)

dashboard_content.css_classes = ['scrollable-content']

# Serve the Panel app
panel_server = pn.serve(dashboard_content, show=False, port=0)

@app.route('/')
def index():
    # Get the Bokeh script
    bokeh_script = server_document(url='http://localhost:{}'.format(panel_server.port), relative_urls=True)
    return render_template('index.html', bokeh_script=bokeh_script)

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)