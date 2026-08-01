import os
import requests
from dotenv import load_dotenv

load_dotenv()

INTERAKT_API_KEY = os.getenv("INTERAKT_API_KEY")
INTERAKT_BASE_URL = "https://api.interakt.ai/v1/public/message/"

PHONE_NUMBER = os.getenv("PHONE_NUMBER")


# ===========================================================
# Common Function
# ===========================================================

def send_message(phone, message):

    headers = {
        "Authorization": f"Basic {INTERAKT_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "data": {
            "countryCode": "+91",
            "phoneNumber": phone,
            "type": "Text",
            "callbackData": "SafeGas AI",
            "message": {
                "text": message
            }
        }
    }

    try:

        response = requests.post(
            INTERAKT_BASE_URL,
            headers=headers,
            json=payload
        )

        print("WhatsApp Status :", response.status_code)
        print(response.text)

        return response.status_code in [200, 201]

    except Exception as e:

        print("Interakt Error :", e)
        return False


# ===========================================================
# Automatic Alert
# ===========================================================

def send_whatsapp_alert(sensor):

    if sensor.risk_level == "SAFE":

        message = f"""
🟢 SafeGas AI

Status : SAFE

No Gas Leakage Detected

Gas : {sensor.gas_level}
Temperature : {sensor.temperature}°C
Humidity : {sensor.humidity}%
Flame : {sensor.flame_status}

Risk Score : {sensor.risk_score}%

Relay1 : {sensor.relay1_status}
Relay2 : {sensor.relay2_status}
Fan : {sensor.fan_status}
Buzzer : {sensor.buzzer_status}
"""

    elif sensor.risk_level == "MEDIUM":

        message = f"""
🟡 SafeGas AI

Status : MEDIUM

Gas level is increasing.

Gas : {sensor.gas_level}
Temperature : {sensor.temperature}°C
Humidity : {sensor.humidity}%
Flame : {sensor.flame_status}

Risk Score : {sensor.risk_score}%

Please inspect your LPG cylinder.
"""

    elif sensor.risk_level == "HIGH":

        message = f"""
🟠 SafeGas AI

HIGH LPG GAS ALERT

Gas : {sensor.gas_level}
Temperature : {sensor.temperature}°C
Humidity : {sensor.humidity}%
Flame : {sensor.flame_status}

Risk Score : {sensor.risk_score}%

Automatic Fan ON
Buzzer ON

Please check immediately.
"""

    else:

        message = f"""
🔴 SafeGas AI

CRITICAL LPG GAS ALERT

Gas : {sensor.gas_level}
Temperature : {sensor.temperature}°C
Humidity : {sensor.humidity}%
Flame : {sensor.flame_status}

Risk Score : {sensor.risk_score}%

EVACUATE IMMEDIATELY

Turn OFF Cylinder
Open Doors
Avoid Fire
Call Emergency Service
"""

    return send_message(PHONE_NUMBER, message)


# ===========================================================
# Chatbot Reply
# ===========================================================

def send_whatsapp_reply(phone, message):

    return send_message(phone, message)