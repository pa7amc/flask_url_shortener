from flask import Flask, request, redirect
import string
import random


app = Flask(__name__)


def id_gen(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


links = {}


@app.route('/add', methods=['PUT'])
def get_url():
    url = request.args.get('url', '')
    key = id_gen()
    links[key] = url
    return links


@app.route('/<id>', methods=['GET'])
def redirect_key(id):
    return redirect(str(links[id]))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
