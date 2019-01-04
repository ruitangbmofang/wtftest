from flask_wtf.csrf import CsrfProtect
from flask import Flask
import config
from app.models import db
from app.views.admin import admin
from app.views.user import user

app = Flask(__name__)
app.config.from_object(config)
mycsrf = CsrfProtect()
mycsrf.init_app(app)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')



@app.route('/')
def homep():
    return 'hello'

if __name__ == '__main__':
    app.run()