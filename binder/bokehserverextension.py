from subprocess import Popen

def load_jupyter_server_extension(nbapp):
"""serve the bokeh-app directory with bokeh server"""
Popen(["bokeh", "serve", "bokeh-app", "--allow-websocket-origin=*"])

#/proxy/5006/bokeh-app