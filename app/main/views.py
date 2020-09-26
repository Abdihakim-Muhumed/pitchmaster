from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User,Pitch,Comment


@main.route('/')
def index():
    pickup = Pitch.get_pitches('pickuplines')
    interview = Pitch.get_pitches('interviewpitch')
    pitches = Pitch.query.all()

    return render_template('index.html', title='Home', interview=interview, pickup = pickup, pitches=pitches)
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)