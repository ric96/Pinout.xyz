#!/usr/bin/env python

import sys

try:
    from flask import Flask, send_from_directory
except ImportError:
    exit("This script requires the Flask module\nInstall with: sudo pip install Flask")


app = Flask(__name__)

lang = 'en'


@app.route('/pinout/')
def show_index():
    return send_from_directory(basedir, 'index.html')


@app.route("/pinout/resources/<path:filename>")
def custom_static(filename):
    return send_from_directory(basedir + 'resources/', filename)


@app.route("/pinout/<path:page>")
def show_page(page):
    return send_from_directory(basedir, page)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        lang = sys.argv[1]

    basedir = 'output/{lang}/pinout/'.format(lang=lang)

    app.run(host='0.0.0.0', debug=True)
