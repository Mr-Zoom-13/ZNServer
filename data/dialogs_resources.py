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
        tmp_dialog = dialog.to_dict(only=(
            'id', 'title', 'avatar'))
        users = [item.to_dict(only=(
            'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
            'place_of_born', 'age', 'status', 'avatar', 'activity_info',
            'last_seen', 'sid'))
            for item in dialog.users]
        messages = [item.to_dict(only=(
            'id', 'user_id', 'dialog_id', 'text', 'date', 'was_read'))
            for item in dialog.messages]
        tmp_dialog['users'] = users
        tmp_dialog['messages'] = messages
        return jsonify(
            {
                'dialog': tmp_dialog
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
        for dialog in dialogs:
            print(dialog.users)
            tmp_dialog = dialog.to_dict(only=(
                    'id', 'title', 'avatar'))
            users = [item.to_dict(only=(
                            'id', 'email', 'surname', 'name', 'birthdate', 'place_of_stay',
                            'place_of_born', 'age', 'status', 'avatar', 'activity_info',
                            'last_seen', 'sid'))
                            for item in dialog.users]
            messages = [item.to_dict(only=(
                            'id', 'user_id', 'dialog_id', 'text', 'date', 'was_read'))
                            for item in dialog.messages]
            tmp_dialog['users'] = users
            tmp_dialog['messages'] = messages
            dialogs_ready.append(tmp_dialog)
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
