from flask import Blueprint, render_template

profile = Blueprint('profile', __name__, template_folder='')


@profile.route('/', methods=['GET'])
def view_profile():
    return render_template('profile.html', title="Merchant Profile")
