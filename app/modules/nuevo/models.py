from app import db


class Nuevo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('user', backref='nuevo', lazy = True)

    def __repr__(self):
        return f'Nuevo<{self.id}>'
