from flask import jsonify, render_template, Blueprint
from got import db
from got.models import battles


blueprint = Blueprint('battles_controller', __name__, url_prefix='/battles')

@blueprint.route("/")
def list():
    characters = db.session.query(Battles).all()
    return jsonify(characters=[dict(battles) for battles in characters])