from app import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    salt = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Match(db.Model):
    match_id = db.Column(db.String(128), primary_key=True)
    home_team = db.Column(db.String(128))
    away_team = db.Column(db.String(128))
    status = db.Column(db.Integer, default=0)
    time = db.Column(db.DateTime(timezone=True))
    result = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Match {}>'.format(self.match_id)


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    value = db.Column(db.String(128))


class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(10))
    value = db.Column(db.Integer)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name="transaction_user"))
    package_id = db.Column(db.Integer, db.ForeignKey('package.id', name="transaction_package"))


class Balance(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name="balance_user"), primary_key=True)
    balance = db.Column(db.Integer, default=0)


class New(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Bet(db.Model):
    __table_args__ = (
        db.UniqueConstraint('user_id', 'match_id'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='bet_user'))
    match_id = db.Column(db.String(128), db.ForeignKey('match.match_id', name='bet_match'))
    value = db.Column(db.Integer)
    prediction = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    availability = db.Column(db.Integer, default=0)
