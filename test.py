from data.dialogs import Dialog
from data.users import User
from data import db_session


db_session.global_init("db/network.db")
db_ses = db_session.create_session()
c = Dialog(title='New')
user = db_ses.query(User).filter(User.id == 1).first()
c.users.append(user)
db_ses.commit()
