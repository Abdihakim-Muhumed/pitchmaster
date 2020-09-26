from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
class User(db.Model):
    ''' class for user model'''
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
     def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    content= db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    postedtime = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship("User", foreign_keys=user_id)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitches(cls, category):
        pitches = cls.query.filter_by(category=category).all()
        return pitches
    @classmethod
    def get_all_pitches(cls):
        pitches = cls.query.all()
        return pitches

    
    @classmethod
    def get_pitch(cls, id):
        pitch = cls.query.filter_by(id=id).first()
        return pitch

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1500))
    postetime = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", foreign_keys=user_id)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, pitch):
        comments = cls.query.filter_by(pitch_id=pitch).all()
        return comments