from flask import Flask, render_template, url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)


@app.route('/')
def show_post():
    #render_template('hello.html')
    a = request.form.get('https://ncov.blog/')
    deaths = request.status.get('https://ncov.blog/')
    return '<p>{deaths: %s}</p>' % deaths


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)

if __name__ == '__main__':
    app.run(debug=True)