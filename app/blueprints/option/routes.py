from flask import Blueprint,render_template

bp = Blueprint('option ', __name__)



@bp.route('/vol_and_skew')
def cad_production():
     return render_template('option/vol_and_skew.html')