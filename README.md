# 🛡️ AI Security Operations Center (SOC) Assistant

An AI-powered SOC analyst that automatically investigates security alerts, maps threats to the MITRE ATT&CK framework, and recommends response actions in real time.

## 🔍 What it does
- Analyzes real Wazuh SIEM alerts automatically
- Explains attack techniques in simple language
- Maps threats to MITRE ATT&CK framework
- Suggests immediate remediation steps
- Determines if alert is real threat or false positive

## 🧱 Tech Stack
- **Python** — core scripting
- **Wazuh** — SIEM alert source (real network alerts)
- **Groq API (Llama3)** — AI analysis engine
- **MITRE ATT&CK** — threat intelligence framework

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/SairaAliBhatti/ai-soc-assistant.git
cd ai-soc-assistant
```

### 2. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install groq python-dotenv
```

### 3. Add your API key
```bash
cp .env.example .env
# Add your Groq API key inside .env
```

### 4. Add Wazuh alerts
```bash
# Pull alerts from your Wazuh instance
ssh wazuh-user@YOUR_WAZUH_IP "sudo tail -50 /var/ossec/logs/alerts/alerts.json" > alerts.json
```

### 5. Run
```bash
python3 soc_assistant.py
```

## 📊 Sample Output
