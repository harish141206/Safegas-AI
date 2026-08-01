console.log("SafeGas AI Dashboard Loaded");

// ===========================================
// Load Latest Sensor Data
// ===========================================

async function loadDashboard() {

    try {

        const response = await fetch("/api/latest");

        if (!response.ok) {
            throw new Error("Failed to fetch sensor data");
        }

        const data = await response.json();

        if (!data || Object.keys(data).length === 0) {
            console.log("No sensor data available.");
            return;
        }

        // Gas Level
        if (document.getElementById("gasLevel"))
            document.getElementById("gasLevel").innerText = data.gas_level;

        // Temperature
        if (document.getElementById("temperature"))
            document.getElementById("temperature").innerText =
                data.temperature + " °C";

        // Humidity
        if (document.getElementById("humidity"))
            document.getElementById("humidity").innerText =
                data.humidity + " %";

        // Flame
        if (document.getElementById("flameStatus"))
            document.getElementById("flameStatus").innerText =
                data.flame_status;

        // Risk Score
        if (document.getElementById("riskScore"))
            document.getElementById("riskScore").innerText =
                data.risk_score + " %";

        // Risk Level
        if (document.getElementById("riskLevel"))
            document.getElementById("riskLevel").innerText =
                data.risk_level;

        // Relay 1
        if (document.getElementById("relay1"))
            document.getElementById("relay1").innerText =
                data.relay1_status;

        // Relay 2
        if (document.getElementById("relay2"))
            document.getElementById("relay2").innerText =
                data.relay2_status;

        // Fan
        if (document.getElementById("fan"))
            document.getElementById("fan").innerText =
                data.fan_status;

        // Buzzer
        if (document.getElementById("buzzer"))
            document.getElementById("buzzer").innerText =
                data.buzzer_status;

        updateRiskColor();

    }

    catch (error) {

        console.error("Dashboard Error :", error);

    }

}

// Load immediately
loadDashboard();

// Refresh every 1 second
setInterval(loadDashboard, 1000);


// ===========================================
// Current Date & Time
// ===========================================

function updateCurrentTime() {

    let now = new Date();

    let options = {

        weekday: "long",

        year: "numeric",

        month: "long",

        day: "numeric",

        hour: "2-digit",

        minute: "2-digit",

        second: "2-digit"

    };

    let currentTime = now.toLocaleString("en-IN", options);

    let timeElement = document.getElementById("currentTime");

    if (timeElement) {

        timeElement.innerHTML = currentTime;

    }

}

updateCurrentTime();

setInterval(updateCurrentTime, 1000);


// ===========================================
// Risk Level Color
// ===========================================

function updateRiskColor() {

    let risk = document.getElementById("riskLevel");

    if (!risk)
        return;

    let level = risk.innerText.trim().toUpperCase();

    risk.classList.remove(
        "safe",
        "medium",
        "high",
        "critical"
    );

    switch (level) {

        case "SAFE":
            risk.classList.add("safe");
            break;

        case "MEDIUM":
            risk.classList.add("medium");
            break;

        case "HIGH":
            risk.classList.add("high");
            break;

        case "CRITICAL":
            risk.classList.add("critical");
            break;
    }

}


// ===========================================
// Window Loaded
// ===========================================

window.onload = function () {

    console.log("Dashboard Ready");

    updateRiskColor();

};