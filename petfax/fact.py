
from flask import Blueprint, render_template

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def form():
    return render_template('pet_form.html')
