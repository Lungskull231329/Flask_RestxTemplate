"""Core models."""

from sqlalchemy import Column, TEXT
from sqlalchemy.orm import relationship


from .model_base import BaseClass


class User(BaseClass):
    """Пользователи"""
    __tablename__ = 'users'
    # __table_args__ = {'schema': 'core', 'comment': 'Пользователи'}
    __table_args__ = {'comment': 'Пользователи'}

    name = Column(TEXT, unique=True, nullable=False, doc='Имя пользователя')
    password_hash = Column(TEXT, nullable=False, doc='Имя пользователя')

    def __repr__(self):
        return "{}".format(self.name)


class File(BaseClass):
    """Информация"""
    __tablename__ = 'file'
    # __table_args__ = {'schema': 'core', 'comment': 'Информация'}
    __table_args__ = {'comment': 'Информация'}

    real_name = Column(TEXT, unique=True, nullable=False, doc='Информация')
    expansion = Column(TEXT, nullable=False, doc='Информация')
    alias_name = Column(TEXT, unique=True, nullable=False, doc='Информация')
    size = Column(TEXT, nullable=False, doc='Информация')
    md5 = Column(TEXT, unique=True, nullable=False, doc='md5')
    note = Column(TEXT, nullable=False, doc='Информация')

    def __repr__(self):
        return "{}".format(self.note)

