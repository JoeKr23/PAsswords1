from db import db


class UsernameModel(db.Model):
    __tablename__ = 'username'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    domain = db.relationship('DomainModel')

    def __init__(self, username, password, domain_id):
        self.username = username
        self.password = password
        self.domain_id = domain_id

    def json(self):
        return {'username': self.username, 'password': self.password}

    @classmethod
    def find_by_name(cls, username):
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
