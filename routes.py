from flask import Blueprint, render_template, jsonify
from models import SensorData, AlertHistory, ChatHistory

routes_bp = Blueprint("routes", __name__)


# ======================================
# Dashboard
# ======================================
@routes_bp.route("/")
@routes_bp.route("/dashboard")
def dashboard():

    latest_sensor = SensorData.query.order_by(
        SensorData.id.desc()
    ).first()

    return render_template(
        "dashboard.html",
        sensor=latest_sensor
    )


# ======================================
# Live Dashboard API
# ======================================
@routes_bp.route("/api/latest")
def latest_sensor():

    sensor = SensorData.query.order_by(
        SensorData.id.desc()
    ).first()

    if sensor is None:

        return jsonify({
            "status": "No Data"
        })

    return jsonify({

        "gas_level": sensor.gas_level,

        "temperature": sensor.temperature,

        "humidity": sensor.humidity,

        "flame_status": sensor.flame_status,

        "risk_score": sensor.risk_score,

        "risk_level": sensor.risk_level,

        "relay1_status": sensor.relay1_status,

        "relay2_status": sensor.relay2_status,

        "fan_status": sensor.fan_status,

        "buzzer_status": sensor.buzzer_status,

        "created_at": sensor.created_at.strftime("%d-%m-%Y %H:%M:%S")

    })


# ======================================
# Sensor History
# ======================================
@routes_bp.route("/history")
def history():

    sensor_history = SensorData.query.order_by(
        SensorData.id.desc()
    ).all()

    return render_template(
        "history.html",
        history=sensor_history
    )


# ======================================
# Alert History
# ======================================
@routes_bp.route("/alerts")
def alerts():

    alerts = AlertHistory.query.order_by(
        AlertHistory.id.desc()
    ).all()

    return render_template(
        "alerts.html",
        alerts=alerts
    )


# ======================================
# Chat History
# ======================================
@routes_bp.route("/chat-history")
def chat_history():

    chats = ChatHistory.query.order_by(
        ChatHistory.id.desc()
    ).all()

    return render_template(
        "chatbot.html",
        chats=chats
    )


# ======================================
# Chatbot
# ======================================
@routes_bp.route("/chatbot")
def chatbot():

    chats = ChatHistory.query.order_by(
        ChatHistory.id.desc()
    ).all()

    return render_template(
        "chatbot.html",
        chats=chats
    )


# ======================================
# Emergency
# ======================================
@routes_bp.route("/emergency")
def emergency():

    latest_sensor = SensorData.query.order_by(
        SensorData.id.desc()
    ).first()

    return render_template(
        "emergency.html",
        sensor=latest_sensor
    )