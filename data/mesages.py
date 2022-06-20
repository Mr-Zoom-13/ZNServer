import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
import datetime


class Message(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'messages'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    dialog_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('dialogs.id'))
    text = sqlalchemy.Column(sqlalchemy.Text)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    was_read = sqlalchemy.Column(sqlalchemy.Integer, default=0) # 0 = wasn't read, 1 = was read
    user = orm.relation('User')
    dialog = orm.relation('Dialog')
