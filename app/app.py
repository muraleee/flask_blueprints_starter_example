from flask import Flask
#from app.blueprints import example_blueprint
from importlib import import_module

app = Flask(__name__)


blueprints = ["basis", "option"]

for bp in blueprints:
    module = import_module(f"app.blueprints.{bp}.routes")
    app.register_blueprint(module.bp, url_prefix=f"/calgary/{bp}")

print(app.url_map)
# module = import_module("app.blueprints.basis.routes")
# app.register_blueprint(module.bp, url_prefix="/calgary/basis")

# module = import_module("app.blueprints.option.routes")
# app.register_blueprint(module.bp, url_prefix="/calgary/option")