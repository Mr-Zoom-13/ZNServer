from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from . import db_session
from .users import User
from .users_parser import post_parser, get_parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_ses = db_session.create_session()
        user = db_ses.query(User).get(user_id)
        return jsonify(
            {
                'user': user.to_dict(only=(
                    'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
                    'place_of_born', 'age', 'status', 'avatar', 'activity_info', 'activity_to',
                    'last_seen', 'sid'))
            }
        )

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        args = get_parser.parse_args()
        if args['type'] == 'check_is_exists':
            user = db_sess.query(User).filter(User.email == args['email']).first()
            if not user:
                return jsonify({'error': 'Not exists'})
            if user.check_password(args['password']):
                return jsonify({'success': user.to_dict(only=(
                    'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
                    'place_of_born', 'age', 'status', 'avatar', 'activity_info', 'activity_to',
                    'last_seen', 'sid'))})
            return jsonify({'error': 'Email exists, but incorrect password'})
        else:
            users = db_sess.query(User).all()
            return jsonify(
                {
                    'users':
                        [item.to_dict(only=(
                            'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
                            'place_of_born', 'age', 'status', 'avatar', 'activity_info',
                            'activity_to',
                            'last_seen', 'sid'))
                            for item in users]
                }
            )

    def post(self):
        db_sess = db_session.create_session()
        args = post_parser.parse_args()
        if db_sess.query(User).filter(User.email == args['email']).first():
            return jsonify({'error': 'This email already exists'})
        user = User(email=args['email'],
                    surname=args['surname'], name=args['name'], birthdate=args['birthdate'],
                    place_of_stay=args['place_of_stay'], place_of_born=args['place_of_born'],
                    age=args['age'], status=args['status'])
        user.set_password(args['password'])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
