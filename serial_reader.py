import serial
import json
import time

from models import (
    db,
    SensorData,
    AlertHistory,
    ChatHistory
)

from interakt_service import send_whatsapp_alert

SERIAL_PORT = "COM8"
BAUD_RATE = 115200

previous_risk_level = None

# --------------------------------------------------
# Connect ESP32
# --------------------------------------------------
try:
    esp32 = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=1
    )

    time.sleep(2)

    print(f"Connected to {SERIAL_PORT}")

except Exception as e:

    print("Unable to connect to ESP32")
    print(e)

    esp32 = None


# --------------------------------------------------
# Read JSON
# --------------------------------------------------
def read_sensor_data():

    if esp32 is None:
        return None

    try:

        if esp32.in_waiting > 0:

            line = esp32.readline().decode(
                "utf-8",
                errors="ignore"
            ).strip()

            if not line:
                return None

            if not line.startswith("{"):
                return None

            print("Received :", line)

            return json.loads(line)

    except json.JSONDecodeError:

        print("Invalid JSON")

    except Exception as e:

        print("Serial Error :", e)

    return None


# --------------------------------------------------
# Save Sensor Data
# --------------------------------------------------
def save_sensor_data(app):

    global previous_risk_level

    with app.app_context():

        data = read_sensor_data()

        if data is None:
            return

        try:

            sensor = SensorData(

                gas_level=data.get("gas_level", 0),

                temperature=data.get("temperature", 0),

                humidity=data.get("humidity", 0),

                flame_status=data.get("flame_status", "NO"),

                risk_score=data.get("risk_score", 0),

                risk_level=data.get("risk_level", "SAFE"),

                relay1_status=data.get("relay1_status", "OFF"),

                relay2_status=data.get("relay2_status", "OFF"),

                fan_status=data.get("fan_status", "OFF"),

                buzzer_status=data.get("buzzer_status", "OFF")

            )

            db.session.add(sensor)
            db.session.commit()

            print("Sensor Data Saved Successfully")

            # ----------------------------------------
            # Save Alert & Chat only if Risk Changes
            # ----------------------------------------

            if previous_risk_level != sensor.risk_level:

                previous_risk_level = sensor.risk_level

                # Alert Message
                if sensor.risk_level == "SAFE":
                    message = "System is operating normally. No gas leakage detected."

                elif sensor.risk_level == "LOW":
                    message = "Low gas concentration detected. Please monitor the area."

                elif sensor.risk_level == "MEDIUM":
                    message = "Medium gas leakage detected. Check the cylinder and regulator."

                elif sensor.risk_level == "HIGH":
                    message = "High gas leakage detected. Exhaust fan activated. Please ventilate immediately."

                elif sensor.risk_level == "DANGER":
                    message = "Danger! Gas leak or fire detected. Gas supply shut off automatically. Evacuate immediately."

                else:
                    message = "Risk status updated."

                # ----------------------------------------
                # Alert History
                # ----------------------------------------

                alert = AlertHistory(

                    risk_score=sensor.risk_score,

                    risk_level=sensor.risk_level,

                    alert_message=message,

                    message_status="Sent"

                )

                db.session.add(alert)

                print("Alert History Saved")

                # ----------------------------------------
                # Chat History
                # ----------------------------------------

                chat = ChatHistory(

                    user_message=f"Current Risk Level : {sensor.risk_level}",

                    bot_reply=message

                )

                db.session.add(chat)

                print("Chat History Saved")

                db.session.commit()

                # ----------------------------------------
                # WhatsApp Alert
                # ----------------------------------------

                send_whatsapp_alert(sensor)

                print("WhatsApp Alert Sent")

        except Exception as e:

            db.session.rollback()

            print("Database Error :", e)


# --------------------------------------------------
# Background Thread
# --------------------------------------------------
def start_serial_reader(app):

    print("Waiting for ESP32 Data...\n")

    while True:

        save_sensor_data(app)

        time.sleep(1)