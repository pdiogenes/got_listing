from flask import jsonify, render_template, Blueprint
from got import db
from got.models import CharacterDeaths


blueprint = Blueprint('character_deaths_controller', __name__, url_prefix='/characterdeaths')

@blueprint.route("/")
def list():
    characters = db.session.query(CharacterDeaths).all()
    return jsonify(characters=[dict(character_deaths) for character_deaths in characters])

