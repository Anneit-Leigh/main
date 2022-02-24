from flask import Flask, render_template, url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/d')
def show_site():
    return render_template('hello.html')
#http://127.0.0.1:5000/d

@app.route('/state')
def show_post():
    #a = request.form.get('https://ncov.blog/')
    deaths = request.headers.get('https://ncov.blog/')
    return '<p>{    deaths:      %s}</p>' % deaths
#http://127.0.0.1:5000/state


@app.route('/state/<value>')
def show_value(value):
    if value=='deaths':
        return  f'{escape(value)} :   393962903'
    else:
        return 'Invalid request'
#http://127.0.0.1:5000/state/deaths


@app.route('/', methods=['GET','POST'])
def index():
    state = request.args.get('state')
    error = None
    if request.method == 'GET':
        return '''
                <h1>The deaths value is: {}</h1>'''.format(state)
    else:
        error = 'Invalid request'
        return error
    # следущий код выполняется при ошибке
    # http://127.0.0.1:5000/?state=deaths

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

if __name__ == '__main__':
    app.run(debug=True)