from flask import Flask, render_template, redirect, jsonify, request, flash
from biaodan import MyForm
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

app = Flask(__name__)

app.config["SECRET_KEY"] = "12345678"
csrf.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    print request.form
    if request.method == "POST"and form.validate_on_submit():
        print form.data
        return 'success'
    else:
        print 'this is a test validate'
    return render_template('/login/index.html', form=form)


@app.route('/success/', methods=['GET', 'POST'])
def home():
    return jsonify({"status": "success"})


@app.route('/fail/', methods=['GET', 'POST'])
def youfail():
    return jsonify({"status": "falis"})

if __name__ == '__main__':
    app.run(debug=True)


