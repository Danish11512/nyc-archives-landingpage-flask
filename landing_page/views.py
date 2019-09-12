from flask import (
    render_template,
    request,
    url_for,
    redirect,
    Flask
 
)

from landing_page import app


@app.route('/')
def index():
    room = request.args.get('room', 'reading')
    return render_template('index.html', room = room)
