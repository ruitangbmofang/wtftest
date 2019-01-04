from flask import render_template, jsonify, request, Blueprint
from app.myForm.login import MyForm

login = Blueprint('admin', __name__)


@login.route('/', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if request.method == "POST"and form.validate_on_submit():
        print form.data
        return 'success'
    else:
        print 'this is a test validate'
    return render_template('/login/index.html', form=form)


@login.route('/success/', methods=['GET', 'POST'])
def home():
    return jsonify({"status": "success"})


@login.route('/fail/', methods=['GET', 'POST'])
def youfail():
    return jsonify({"status": "falis"})




