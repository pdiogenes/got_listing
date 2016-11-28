from flask import render_template
from got import app
from got.controllers import battles, character_deaths, character_predictions

app.register_blueprint(battles)
app.register_blueprint(character_deaths)
app.register_blueprint(character_predictions)

app.run()