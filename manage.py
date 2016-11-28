from flask import render_template
from got import app
from got.controllers import battles, character_deaths, character_predictions

app.register_blueprint(got)
app.register_blueprint(home)
app.run()