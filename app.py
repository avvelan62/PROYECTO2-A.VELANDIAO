from flask import Flask, redirect, url_for
from dotenv import load_dotenv
from database.db import db, init_db, load_models
from controllers.heladeria_controller import heladeria_blueprint
import os

load_dotenv(override=True)
app = Flask(__name__, template_folder="views")
app.secret_key = '12345'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
init_db(app) # Comentar para entorno de producción
load_models(app)

app.register_blueprint(heladeria_blueprint)

# Redirigir la raíz al blueprint
@app.route('/')
def home():
    return redirect(url_for('heladeria_bp.index')) 
