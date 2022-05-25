from config import api, app, socket_app
from flask import render_template
from data import db_session, users_resources
from sockets import SocketClass


@app.route('/')
def sockets():
    return render_template('index.html')


def main():
    db_session.global_init("db/network.db")
    api.add_resource(users_resources.UsersListResource, '/api/v1/users')
    api.add_resource(users_resources.UsersResource, '/api/v1/users/<int:user_id>')
    socket_app.on_namespace(SocketClass('/'))
    socket_app.run(app)


if __name__ == '__main__':
    main()
