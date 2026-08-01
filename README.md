# 🔥 SafeGas AI
## AI-Powered Smart LPG Cylinder Safety & Accident Prevention System

**Tagline:** *Predict Before It Leaks, Protect Before It Explodes*

---

# 📌 Project Overview

SafeGas AI is an IoT and AI-powered smart safety system designed to monitor LPG cylinder conditions in real time and help prevent gas leakage-related accidents. The system continuously monitors gas concentration, temperature, humidity, and flame conditions using multiple sensors connected to an ESP32 microcontroller.

Sensor data is transmitted to a Python Flask backend through serial communication, stored in an SQLite database, and analyzed for safety monitoring. The project also integrates an AI-powered WhatsApp chatbot using Interakt, OpenAI API, and ngrok, enabling users to receive instant safety guidance and automated responses through WhatsApp.

This project combines Embedded Systems, IoT, Artificial Intelligence, Cloud Communication, and Web Technologies into a single smart safety solution.

---

# 🚨 Problem Statement

LPG gas leakage is one of the major causes of household and industrial accidents.

Current gas detection systems generally provide alerts only after gas leakage has already occurred. Many systems also lack remote monitoring, intelligent analysis, and customer support capabilities.

The objective of SafeGas AI is to develop an intelligent, real-time safety monitoring system capable of:

- Detecting LPG gas leakage
- Monitoring temperature and humidity
- Detecting fire hazards
- Providing instant alerts
- Supporting users through an AI-powered WhatsApp chatbot

---

# 💡 Proposed Solution

SafeGas AI consists of two major modules:

## Module 1 – Smart IoT Monitoring

- Real-time gas leakage detection
- Temperature monitoring
- Humidity monitoring
- Flame detection
- Sensor data logging
- Safety monitoring

## Module 2 – AI WhatsApp Assistant

- WhatsApp chatbot
- AI-generated responses
- LPG safety guidance
- Customer support
- Frequently Asked Questions
- Emergency information

---

# 🎯 Objectives

- Develop an intelligent LPG monitoring system.
- Detect gas leakage before dangerous conditions.
- Monitor environmental parameters continuously.
- Store sensor data for future analysis.
- Integrate AI-powered customer assistance.
- Improve LPG safety using IoT and Artificial Intelligence.

---

# 🏗️ System Architecture

```
                     LPG Cylinder
                           │
                           │
         ┌─────────────────────────────────┐
         │           Sensors              │
         │                                │
         │ • MQ-2 Gas Sensor              │
         │ • DHT11 Temperature Sensor     │
         │ • Flame Sensor                 │
         └─────────────────────────────────┘
                           │
                           │
                     ESP32 Controller
                           │
                           │
                 Serial Communication
                           │
                           │
                   Flask Backend Server
                           │
            ┌──────────────┴──────────────┐
            │                             │
            │                             │
      SQLite Database              OpenAI API
                                          │
                                          │
                               Interakt WhatsApp API
                                          │
                                          │
                                  ngrok Webhook
                                          │
                                          │
                               AI WhatsApp Assistant
```

---

# ⚙️ Working Principle

### Step 1

ESP32 continuously reads:

- Gas concentration
- Temperature
- Humidity
- Flame status

---

### Step 2

Sensor values are converted into JSON format.

Example:

```json
{
  "gas": 245,
  "temperature": 31,
  "humidity": 61,
  "flame": 0
}
```

---

### Step 3

The Flask backend receives sensor data through serial communication.

---

### Step 4

Sensor readings are stored in SQLite Database.

---

### Step 5

Users communicate with the AI chatbot through WhatsApp.

---

### Step 6

Interakt forwards the message to the Flask webhook.

---

### Step 7

Flask sends the user query to OpenAI API.

---

### Step 8

The AI-generated response is returned to the user through WhatsApp.

---

# 🤖 AI Chatbot Workflow

```
User
   │
   │
WhatsApp
   │
   │
Interakt API
   │
   │
Flask Webhook
   │
   │
OpenAI API
   │
   │
AI Response
   │
   │
WhatsApp Reply
```

---

# 📡 IoT Data Flow

```
Sensors

↓

ESP32

↓

Serial Communication

↓

Flask Backend

↓

SQLite Database

↓

Monitoring Dashboard
```

---

# 🔧 Hardware Components

| Component | Purpose |
|------------|------------------------------|
| ESP32 | Main Controller |
| MQ-2 Gas Sensor | LPG Leakage Detection |
| DHT11 | Temperature & Humidity |
| Flame Sensor | Fire Detection |
| Relay Module | Automatic Control |
| Buzzer | Warning Alert |
| Jumper Wires | Connections |
| USB Cable | Programming & Communication |

---

# 🔌 ESP32 Pin Configuration

| Component | ESP32 Pin |
|------------|------------|
| MQ-2 Sensor | GPIO 34 |
| DHT11 | GPIO 4 |
| Flame Sensor | GPIO 5 |
| Relay | GPIO 19 |
| Buzzer | GPIO 18 |

---

# 💻 Software Requirements

## Programming Languages

- Python
- Embedded C

## Backend

- Flask
- Flask-SQLAlchemy
- SQLite
- PySerial

## AI

- OpenAI API

## Communication

- Interakt WhatsApp Business API

## Tunnel

- ngrok

## Development Tools

- Arduino IDE
- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```
SafeGas-AI

│
├── backend
│   ├── app.py
│   ├── webhook.py
│   ├── openai_service.py
│   ├── interakt_service.py
│   ├── requirements.txt
│   ├── database
│   │     └── safegas.db
│   └── README.md
│
├── esp32
│   └── safegas_esp32.ino
│
├── presentations
│
├── demo_video
│
└── README.md
```

---

# 🚀 Installation

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Backend

```bash
python app.py
```

---

## Start ngrok

```bash
ngrok http 5000
```

---

# 🔐 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key

INTERAKT_API_KEY=your_interakt_api_key

NGROK_AUTH_TOKEN=your_ngrok_auth_token
```

---

# 🗄️ Database

Database Name

```
safegas.db
```

Stored Parameters

- Gas Value
- Temperature
- Humidity
- Flame Status
- Timestamp

---

# ⚠️ Troubleshooting

## ESP32 Not Connected

- Check USB cable.
- Verify COM Port.
- Install ESP32 Drivers.

---

## COM Port Access Denied

Disable Flask auto-reloader:

```python
app.run(
    host="0.0.0.0",
    port=5000,
    debug=False,
    use_reloader=False
)
```

---

## ngrok Not Working

Authenticate ngrok:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

Start tunnel:

```bash
ngrok http 5000
```

---

# 🔮 Future Enhancements

- Machine Learning based LPG Risk Prediction
- Automatic Gas Valve Shutoff
- Mobile Application
- Cloud Deployment
- Voice-based WhatsApp Assistant
- Multi-language Support
- Smart Dashboard
- Predictive Analytics

---

# 🌍 Applications

- Smart Homes
- Restaurants
- Hotels
- Commercial Kitchens
- LPG Distribution Centers
- Industrial Safety
- Smart City Applications

---

# 🏆 Innovation Highlights

- IoT-Based LPG Monitoring
- AI-Powered WhatsApp Assistant
- Real-Time Sensor Monitoring
- OpenAI Integration
- Interakt API Integration
- Flask Backend
- SQLite Database
- ngrok Webhook Integration
- Scalable Architecture

---

# 👥 Team Details

## **Project Title**

**SafeGas AI – AI-Powered Smart LPG Cylinder Safety & Accident Prevention System**

### **Team Members**

| Name | Department |
|------|------------|
| **Harish Raj G** | Electronics and Communication Engineering |
| **Siranjeevi K** | Electronics and Communication Engineering |
| **Suresh V** | Electronics and Communication Engineering |

---

## College

**Renganayagi Varatharaj College of Engineering**

Sivakasi, Tamil Nadu, India

---

# 👨‍💻 Developed By

**Team SafeGas AI**

Department of Electronics and Communication Engineering

Renganayagi Varatharaj College of Engineering

---

# 📜 License

This project was developed as part of a Hackathon for educational, research, and innovation purposes.

© 2026 Team SafeGas AI. All Rights Reserved.