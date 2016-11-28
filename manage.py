from flask import render_template
from got import app
from got.controllers import battles_controller, character_controller, character_predictions_controller

app.register_blueprint(got)
app.register_blueprint(home)
app.run()