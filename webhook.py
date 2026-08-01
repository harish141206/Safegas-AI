from flask import Blueprint, request, jsonify

from models import db, ChatHistory
from openai_service import chatbot_reply
from interakt_service import send_whatsapp_reply

webhook_bp = Blueprint("webhook", __name__)


# ==========================================================
# Website Chatbot API
# ==========================================================
@webhook_bp.route("/api/chat", methods=["POST"])
def website_chat():

    try:

        data = request.get_json()

        user_message = data.get("message", "").strip()

        if user_message == "":
            return jsonify({
                "reply": "Please enter a message."
            })

        ai_reply = chatbot_reply(user_message)

        chat = ChatHistory(
            user_message=user_message,
            bot_reply=ai_reply
        )

        db.session.add(chat)
        db.session.commit()

        return jsonify({
            "reply": ai_reply
        })

    except Exception as e:

        db.session.rollback()

        print(e)

        return jsonify({
            "reply": "Sorry, something went wrong."
        }), 500


# ==========================================================
# Interakt WhatsApp Webhook
# ==========================================================
@webhook_bp.route("/webhook", methods=["POST"])
def webhook():

    try:

        data = request.get_json()

        print("Webhook Received")
        print(data)

        phone_number = (
            data.get("data", {})
                .get("customer", {})
                .get("phone")
        )

        if not phone_number:
            return jsonify({
                "status": "invalid phone"
            }), 400

        message = data.get("data", {}).get("message", {})

        if "text" not in message:
            return jsonify({
                "status": "ignored"
            }), 200

        user_message = message["text"]["body"]

        print("Phone :", phone_number)
        print("Message :", user_message)

        ai_reply = chatbot_reply(user_message)

        chat = ChatHistory(
            user_message=user_message,
            bot_reply=ai_reply
        )

        db.session.add(chat)
        db.session.commit()

        send_whatsapp_reply(
            phone_number,
            ai_reply
        )

        return jsonify({
            "status": "success"
        }), 200

    except Exception as e:

        db.session.rollback()

        print("Webhook Error :", e)

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
    