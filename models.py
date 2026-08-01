from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()


# ==================================================
# Sensor Data
# ==================================================
class SensorData(db.Model):
    __tablename__ = "sensor_data"

    id = db.Column(db.Integer, primary_key=True)

    gas_level = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)

    flame_status = db.Column(db.String(20), nullable=False)

    risk_score = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)

    relay1_status = db.Column(db.String(20), nullable=False)
    relay2_status = db.Column(db.String(20), nullable=False)

    fan_status = db.Column(db.String(20), nullable=False)
    buzzer_status = db.Column(db.String(20), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<SensorData {self.id}>"


# ==================================================
# WhatsApp Alert History
# ==================================================
class AlertHistory(db.Model):
    __tablename__ = "alert_history"

    id = db.Column(db.Integer, primary_key=True)

    risk_score = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)

    alert_message = db.Column(db.Text, nullable=False)

    message_status = db.Column(
        db.String(30),
        default="Sent"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<AlertHistory {self.id}>"


# ==================================================
# AI Chat History
# ==================================================
class ChatHistory(db.Model):
    __tablename__ = "chat_history"

    id = db.Column(db.Integer, primary_key=True)

    user_message = db.Column(
        db.Text,
        nullable=False
    )

    bot_reply = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<ChatHistory {self.id}>"