from flask import jsonify, render_template, Blueprint
from got import db
from got.models import CharacterPredictions


blueprint = Blueprint('character_predictions', __name__, url_prefix='/characterpredictions')

@blueprint.route("/")
def list():
    characters = db.session.query(CharacterPredictions).all()
    return jsonify(characters=[dict(character_predictions) for character_predictions in characters])