#!/usr/bin/env python3
"""4-app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """Config class."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('4-app.Config')
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get_locale method for localeselector."""
    if 'locale' in request.args and \
       request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """Render hello world template."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
