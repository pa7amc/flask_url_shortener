from flask import Flask, request, redirect, render_template
import string
import random


app = Flask(__name__)


def id_gen(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


links = {}


@app.route('/add', methods=['POST'])
def get_url():
    url = request.form.get('url', '')
    key = id_gen()
    links[key] = url
    return render_template('add.html', links=links, url=url, key=key)


@app.route('/<id>', methods=['GET'])
def redirect_key(id):
    return redirect(str(links[id]))


@app.route('/list')
def get_links():
    return render_template('list.html', links=links)


@app.route('/', methods=['GET'])
def home():

    return render_template('home.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
