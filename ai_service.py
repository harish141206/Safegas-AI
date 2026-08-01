from models import SensorData

# ==================================================
# Calculate Risk
# ==================================================
def calculate_risk(sensor):

    gas = sensor.gas_level
    temp = sensor.temperature
    flame = sensor.flame_status

    risk_score = 0

    # -----------------------------
    # Gas Level
    # -----------------------------
    if gas < 250:
        risk_score += 10

    elif gas < 400:
        risk_score += 30

    elif gas < 600:
        risk_score += 60

    else:
        risk_score += 90

    # -----------------------------
    # Temperature
    # -----------------------------
    if temp > 35:
        risk_score += 10

    if temp > 45:
        risk_score += 20

    # -----------------------------
    # Flame
    # -----------------------------
    if flame == "YES":
        risk_score += 30

    if risk_score > 100:
        risk_score = 100

    # -----------------------------
    # Risk Level
    # -----------------------------
    if risk_score <= 30:
        level = "SAFE"

    elif risk_score <= 60:
        level = "MEDIUM"

    elif risk_score <= 80:
        level = "HIGH"

    else:
        level = "CRITICAL"

    # -----------------------------
    # Device Control
    # -----------------------------
    if level in ["HIGH", "CRITICAL"]:

        sensor.relay1_status = "ON"
        sensor.relay2_status = "ON"
        sensor.fan_status = "ON"
        sensor.buzzer_status = "ON"

    else:

        sensor.relay1_status = "OFF"
        sensor.relay2_status = "OFF"
        sensor.fan_status = "OFF"
        sensor.buzzer_status = "OFF"

    sensor.risk_score = risk_score
    sensor.risk_level = level

    return {
        "risk_score": risk_score,
        "risk_level": level,
        "relay1": sensor.relay1_status,
        "relay2": sensor.relay2_status,
        "fan": sensor.fan_status,
        "buzzer": sensor.buzzer_status
    }


# ==================================================
# Analyse Latest Sensor
# ==================================================
def analyse_latest_sensor():

    latest = SensorData.query.order_by(
        SensorData.id.desc()
    ).first()

    if latest is None:
        return None

    return calculate_risk(latest)


# ==================================================
# SafeGas AI Chatbot
# ==================================================
def get_chatbot_reply(message):

    msg = message.lower()

    if "gas" in msg:
        return "The MQ2 gas sensor continuously monitors LPG gas concentration. If gas leakage is detected, SafeGas AI calculates the risk level automatically."

    elif "temperature" in msg:
        return "The DHT sensor measures the surrounding temperature. High temperatures increase the overall risk score."

    elif "humidity" in msg:
        return "The DHT sensor also monitors humidity for environmental analysis."

    elif "flame" in msg or "fire" in msg:
        return "The flame sensor detects the presence of fire. If a flame is detected, the risk score increases immediately."

    elif "risk" in msg:
        latest = analyse_latest_sensor()

        if latest:
            return f"Current Risk Level: {latest['risk_level']} (Risk Score: {latest['risk_score']})"

        return "No sensor data is currently available."

    elif "fan" in msg:
        return "The exhaust fan turns ON automatically during HIGH or CRITICAL risk conditions."

    elif "relay" in msg:
        return "Relay 1 controls the gas valve. Relay 2 controls emergency devices."

    elif "buzzer" in msg:
        return "The buzzer alerts nearby people whenever HIGH or CRITICAL risk is detected."

    elif "safegas" in msg:
        return "SafeGas AI is an AI-powered LPG gas leakage detection and accident prevention system."

    elif "hello" in msg or "hi" in msg:
        return "Hello! I am SafeGas AI. How can I help you today?"

    else:
        return (
            "I can help you with gas leakage detection, "
            "risk level, flame detection, temperature, "
            "humidity, relay status, fan status, and "
            "SafeGas AI system information."
        )