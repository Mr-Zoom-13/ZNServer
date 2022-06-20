from flask import Flask, render_template, request
import base64
from data import db_session
from data.users import User
from data.dialogs import Dialog

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db_session.global_init("db/network_archive.db")
        db_ses = db_session.create_session()
        c = request.files['file'].save(r'C:\Users\Aleksandr\Desktop\Проекты Python\ZoomNetworkServer\1.png')
        with open("1.png", "rb") as image_file:
            user = db_ses.query(Dialog).filter(Dialog.id == 7).first()
            encoded_string = base64.b64encode(image_file.read())
            user.avatar = encoded_string
            db_ses.commit()
            print(encoded_string)
    return render_template('test.html')


@app.route('/image')
def index_2():
    return render_template('test2.html')


app.run(port=5002)