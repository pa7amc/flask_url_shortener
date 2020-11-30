from flask import Flask, request, redirect, render_template
import string
import random


app = Flask(__name__)


def id_gen(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


links = {}


# @app.route('/add', methods=['PUT'])
# def get_url():
#    url = request.args.get('url', '')
#    key = id_gen()
#    links[key] = url
#    return str(key) + " : " + str(links[key])


@app.route('/<id>', methods=['GET'])
def redirect_key(id):
    return redirect(str(links[id]))


# @app.route('/listt', methods=['GET'])
# def get_links():
 #   return links


@app.route('/list')
def get_links():
    return render_template('list.html', links=links)


@app.route('/', methods=['GET', 'POST'])
def home():
    # if hitting the submit post input
    if request.method == 'POST':
        url_ins = request.form["url"]
        print(url_ins)
        key = id_gen()
        links[key] = url_ins
        return str(key) + " : " + str(links[key])
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
