from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify
from . import db_session
from .dialogs import Dialog
from .dialogs_parser import parser


def abort_if_user_not_found(dialog_id):
    session = db_session.create_session()
    user = session.query(Dialog).get(dialog_id)
    if not user:
        abort(404, message=f"User {dialog_id} not found")


class DialogsResource(Resource):
    def get(self, dialog_id):
        abort_if_user_not_found(dialog_id)
        db_ses = db_session.create_session()
        dialog = db_ses.query(Dialog).get(dialog_id)
        return jsonify(
            {
                'dialog': dialog.to_dict(only=(
                    'id', 'title', 'avatar', 'users'))
            }
        )

    def delete(self, dialog_id):
        abort_if_user_not_found(dialog_id)
        db_sess = db_session.create_session()
        dialog = db_sess.query(Dialog).get(dialog_id)
        db_sess.delete(dialog)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class DialogsListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        dialogs = db_sess.query(Dialog).all()
        dialogs_ready = []
        for i in dialogs:
            print(i.users)
            some_dialog = i.to_dict(only=(
                    'id', 'title', 'avatar'))
            some_users = [item.to_dict(only=(
                            'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
                            'place_of_born', 'age', 'status', 'avatar', 'activity_info',
                            'activity_to',
                            'last_seen', 'sid'))
                            for item in i.users]
            some_dialog['users'] = some_users
            dialogs_ready.append(some_dialog)
        return jsonify(
            {
                'dialogs': dialogs_ready
            }
        )

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        dialog = Dialog(title=args['title'], avatar=args['avatar'])
        db_sess.add(dialog)
        db_sess.commit()
        return jsonify({'success': 'OK'})
