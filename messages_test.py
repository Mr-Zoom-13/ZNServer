from data import db_session
from data.dialogs import Dialog
from data.users import User
from data.mesages import Message

db_session.global_init('db/network.db')
db_sess = db_session.create_session()
user = User(email="1@mail.ru")
user.set_password('123')
c = Dialog(title='Di1')
c.users.append(user)
db_sess.add(c)
db_sess.commit()
dialog = db_sess.query(Dialog).get(1)
message = Message(user_id=1, dialog_id=1, text='hi, friend')
dialog.messages.append(message)
db_sess.commit()
dialog = db_sess.query(Dialog).get(1)
print(dialog.messages)