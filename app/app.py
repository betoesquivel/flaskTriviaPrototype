from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__, static_folder="../static", static_url_path="/static")
app.debug = True


@app.route('/')
def index():
    return render_template('index.jinja2.html')

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
