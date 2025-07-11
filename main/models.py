from main.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(120), nullable=False)
    domain = db.Column(db.String(100), nullable=False)
    email_sent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.email_id}>"
