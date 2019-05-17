import datetime
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    posts = db.relationship('StreamLog', backref='user', lazy='dynamic')



class StreamLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.String(64))
    ip = db.Column(db.String(64))
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    timestamp=db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<StreamLog {}.{}>'.format(self.user_id,self.content_id)   

    
