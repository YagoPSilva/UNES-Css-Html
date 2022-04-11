from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Colum(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username


class Tickt(db.Model):
   __tablename__ = 'tickts'
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.Text, nullable=False)
   subject = db.Colum(db.String(80), nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)

   def __init__(self, content, subject, email):
        self.content = content
        self.subject = subject
        self.email = email


        def __repr__(self):
            return '<Tickt %r>' % self.id 