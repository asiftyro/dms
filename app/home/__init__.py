from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='')


@home.route('/', methods=['GET'])
def homepage():
    return render_template('home.html', title="Elow, Wald!")
