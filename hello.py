from flask import Flask, render_template, url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/state/deaths')
def show_post():
    return render_template('hello.html')


@app.route('/user/<username>')
def show_user_profile(username):
    #return f'User {escape(username)}'
    return 'User %s' % username


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)

if __name__ == '__main__':
    app.run(debug=True)