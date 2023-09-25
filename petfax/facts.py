from flask import Blueprint, render_template

# Define a Blueprint for the facts routes
bp = Blueprint('fact', __name__, url_prefix="/facts")

# Define the route for submitting new facts
@bp.route('/new')
def new():
    return render_template('facts/new.html')