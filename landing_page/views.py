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
    room = int(request.args.get('room', '001'))
    return render_template('index.html', room = room)
