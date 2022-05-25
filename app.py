from config import api, app, socket_app
from flask import render_template
from data import db_session, users_resources
from sockets import SocketClass
from data.users import User
import datetime


@app.route('/')
def sockets():
    return render_template('index.html')


def main():
    db_session.global_init("db/network.db")
    db_ses = db_session.create_session()
    for i in db_ses.query(User).all():
        if i.last_seen == 'online':
            i.last_seen = str(datetime.date.today())
        i.sid = '[]'
    db_ses.commit()
    api.add_resource(users_resources.UsersListResource, '/api/v1/users')
    api.add_resource(users_resources.UsersResource, '/api/v1/users/<int:user_id>')
    socket_app.on_namespace(SocketClass('/'))
    socket_app.run(app)


if __name__ == '__main__':
    main()
