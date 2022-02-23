from crypt import methods
from flask import Flask, make_response, render_template, request, post
from flask import url_for
from markupsafe import escape
from hello import app

app = Flask(__name__)

#http://127.0.0.1:5000/index?state=deaths

@app.route('/', methods=['GET','POST'])
def index():
    state = request.args.get('state')
    if request.method == 'GET':
        return '''
                <h1>The deaths value is: {}</h1>'''.format(state)


if __name__ == '__main__':
    app.run(debug=True)