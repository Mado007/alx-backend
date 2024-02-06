#!/usr/bin/env python3
"""7-app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


class Config():
    """Config class."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('7-app.Config')
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    """get user dict."""
    if request.args.get('login_as'):
        try:
            user_id = int(request.args.get('login_as'))
        except Exception:
            return None

        return users.get(user_id)

    else:
        return None


@app.before_request
def before_request():
    """Method that finds the user and sets the login information as global on
    flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """get_locale method for localeselector."""
    if 'locale' in request.args and \
       request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    elif g.user:
        user_local = g.user.get("locale")
        if user_local in app.config['LANGUAGES']:
            return user_local

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """get_timezone method for timezoneselector."""
    try:
        tz = None
        if 'timezone' in request.args:
            tz = request.args['timezone']
        elif g.user and g.user.get("timezone"):
            tz = g.user.get('timezone')
        return timezone(tz).zone
    except UnknownTimeZoneError:
        pass

    return 'UTC'


@app.route('/')
def hello_world():
    """Render hello world template."""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
