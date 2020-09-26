from flask import render_template
from flask_login import login_required


@main.route('/')
def index():
    return render_template('Index.html')

@main.route('/profile.html')
def view_profile():
    render_template('profile.html')
