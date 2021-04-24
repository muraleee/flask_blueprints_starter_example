from flask import Blueprint, render_template

bp = Blueprint('basis', __name__)



@bp.route('/cad_production')
def cad_production():
    return render_template('basis/cad_production.html')