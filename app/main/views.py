from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .forms import PitchForm,CommentForm,EditProfileForm
from .. import db


@main.route('/')
def index():
    pickup = Pitch.get_pitches('pickuplines')
    interview = Pitch.get_pitches('interviewpitch')
    pitches = Pitch.query.all()

    return render_template('index.html', title='Home', interview=interview, pickup = pickup, pitches=pitches)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch_title = form.pitch_title.data
        pitch_content = form.pitch_content.data
        category = form.category.data

        # Updated pitch instance
        new_pitch = Pitch(title=pitch_title, content=pitch_content, category = category, user_id = current_user.id)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index' ))

    
    title = 'New pitch'
    return render_template('new_pitch.html',title = title,form = form)

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interviewpitch')
    return render_template('interview.html', pitches = pitches)

@main.route('/pitches/pickup_lines')
def pickup_lines():

    pitches = Pitch.get_pitches('pickuplines')

    return render_template("pickup.html", pitches = pitches)

@main.route('/pitch/view/<pitch_id>', methods=['GET', 'POST'])
def view_pitch(pitch_id):
   

    pitch = Pitch.query.filter_by(id=pitch_id).first()
    
    comments = Comment.get_comments(pitch_id)
    comment_form = CommentForm()
    if current_user.is_authenticated:
        
        if comment_form.validate_on_submit():
            comments = comment_form.description.data

            new_comment = Comment(comment=comments,user_id=current_user.id,pitch_id = pitch_id)

            new_comment.save_comment()
            
            return redirect(url_for('.view_pitch',pitch_id=pitch_id))
        comments = Comment.get_comments(pitch_id)

        
    return render_template('pitch.html', pitch=pitch, comments=comments, pitch_id=pitch.id, comment_form = comment_form)




@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def edit_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = EditProfileForm()

    if form.validate_on_submit():
        user.bio=form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/edit_profile.html',form =form)






