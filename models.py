from app import db
from app import session
from app import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birth_day = db.Column(db.DATE, nullable=False)
    address = db.Column(db.Text, nullable=False)
    phones = relationship('Phone', backref='user', lazy=True, cascade="all, delete-orphan")
    emails = relationship('Email', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.patronymic = kwargs.get('patronymic')
        self.gender = kwargs.get('gender')
        self.birth_day = kwargs.get('birth_day')
        self.address = kwargs.get('address')

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
                session.commit()
        except Exception:
            session.rollback()
            raise

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    @classmethod
    def get_user(cls, name, surname, patronymic):
        try:
            item = cls.query.filter(
                cls.name == name,
                cls.surname == surname,
                cls.patronymic == patronymic
            ).first()
            if not item:
                raise Exception('No user with this full name')
        except Exception:
            session.rollback()
            raise
        return item

    def __repr__(self):
        return '{}'.format(self.surname)

    @classmethod
    def get_user_by_id(cls, user_id):
        try:
            item = cls.query.filter(cls.id == user_id).first()
            if not item:
                raise Exception('No user with this id')
        except Exception:
            session.rollback()
            raise
        return item


class Phone(Base):
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(12), nullable=False, unique=True)
    phone_type = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        self.phone_number = kwargs.get('phone_number')
        self.phone_type = kwargs.get('phone_type')

    @classmethod
    def get(cls, user_id, phone_id):
        try:
            item = cls.query.filter(
                user_id == user_id,
                phone_id == phone_id
            ).first()
            if not item:
                raise Exception('No phone with this id')
        except Exception:
            session.rollback()
            raise
        return item

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
                session.commit()
        except Exception:
            session.rollback()
            raise

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def __repr__(self):
        return '{}'.format(self.phone_number)


class Email(Base):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    email_type = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        self.email = kwargs.get('email')
        self.email_type = kwargs.get('email_type')

    @classmethod
    def get(cls, user_id, email_id):
        try:
            item = cls.query.filter(
                user_id == user_id,
                email_id == email_id
            ).first()
            if not item:
                raise Exception('No email with this id')
        except Exception:
            session.rollback()
            raise
        return item

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
                session.commit()
        except Exception:
            session.rollback()
            raise

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def __repr__(self):
        return '{}'.format(self.email)
