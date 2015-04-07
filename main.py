from flask import Flask, make_response, abort

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>this document carries a cookies!</h1>')
    response.set_cookie('answer', '43')
    return response


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name


@app.route('/user/<id>')
def get_user(id):
    print id
    if int(id) == 0:
        abort(404)

    return '<h1> Hello, %d!</h1>' % id

if __name__ == '__main__':
    app.run(debug=True)
