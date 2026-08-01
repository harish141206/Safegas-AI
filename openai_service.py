import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ==========================================
# OpenAI Configuration
# ==========================================

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# ==========================================
# AI Safety Analysis
# ==========================================

def analyze_sensor_data(sensor):

    prompt = f"""
You are an AI LPG Safety Assistant.

Analyze the following sensor values.

Gas Level: {sensor.gas_level} ppm
Temperature: {sensor.temperature} °C
Humidity: {sensor.humidity} %
Flame Status: {sensor.flame_status}

Risk Score: {sensor.risk_score}
Risk Level: {sensor.risk_level}

Give the response in the following format.

1. Problem
2. Risk Level
3. Possible Reason
4. Safety Advice

Keep the response short and easy to understand.
"""

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[
                {
                    "role": "system",
                    "content": "You are a Smart LPG Safety Assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3

        )

        return response.choices[0].message.content

    except Exception as e:

        print("OpenAI Error :", e)

        return "Unable to analyze sensor data."


# ==========================================
# Chatbot Conversation
# ==========================================

def chatbot_reply(user_message):

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "system",
                    "content": """
You are SafeGas AI.

You help users with

• LPG Gas Leakage
• Fire Safety
• Emergency Instructions
• Sensor Data
• Smart Home Safety

Always reply in simple English.
"""
                },

                {
                    "role": "user",
                    "content": user_message
                }

            ],

            temperature=0.5

        )

        return response.choices[0].message.content

    except Exception as e:

        print("OpenAI Error :", e)

        return "Sorry, I am unable to answer your question."