from flask import Flask, request, redirect
from url_shortener import id_gen

app = Flask(__name__)


links = {}


@app.route('/add')
def get_url():
    url = request.args.get('url', '')
    key = id_gen()
    links[key] = url
    return links


@app.route('/search')
def redirect_key():
    key = request.args.get('key', '')
    return redirect(str(links[key]))