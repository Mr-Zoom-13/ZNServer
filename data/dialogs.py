import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm

association_table_users = sqlalchemy.Table(
    'user_to_dialog',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('dialogs', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('dialogs.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)

association_table_messages = sqlalchemy.Table(
    'message_to_dialog',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('dialogs', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('dialogs.id')),
    sqlalchemy.Column('messages', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('messages.id'))
)


class Dialog(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'dialogs'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    avatar = sqlalchemy.Column(sqlalchemy.String)
    users = orm.relation('User', secondary="user_to_dialog", backref="dialogs")
    messages = orm.relation('Message', secondary="message_to_dialog", backref="dialogs")
