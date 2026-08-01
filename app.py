from flask import Flask
import threading
import os

from models import db
from routes import routes_bp
from webhook import webhook_bp
from serial_reader import start_serial_reader

# ==================================================
# Flask App
# ==================================================
app = Flask(__name__)

# Absolute database path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_FOLDER = os.path.join(BASE_DIR, "database")

# Create database folder if it doesn't exist
os.makedirs(DB_FOLDER, exist_ok=True)

DB_PATH = os.path.join(DB_FOLDER, "safegas.db")

print("Current Directory :", BASE_DIR)
print("Database Path     :", DB_PATH)
print("Database Exists   :", os.path.exists(DB_PATH))

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(routes_bp)
app.register_blueprint(webhook_bp)

# Create Tables
with app.app_context():
    db.create_all()
    print("Database Connected Successfully!")

# Start ESP32 Serial Reader
serial_thread = threading.Thread(
    target=start_serial_reader,
    args=(app,),
    daemon=True
)
serial_thread.start()

# Run Flask
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )