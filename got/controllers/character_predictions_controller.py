from flask import jsonify, render_template, Blueprint
from got import db
from got.models import CharacterPredictions


blueprint = Blueprint('got_controller', __name__, url_prefix='/characterpredictions')

@blueprint.route("/json")
def list():
    characters = db.session.query(CharacterPredictions).all()
    return jsonify(characters=[dict(character_predictions) for character_predictions in characters])