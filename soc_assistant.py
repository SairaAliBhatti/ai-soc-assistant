import os
import json
import subprocess
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_alert(alert):
    prompt = f"""
    You are an expert SOC analyst. Analyze this security alert and provide:
    1. What happened (simple terms)
    2. Severity level (Critical/High/Medium/Low)
    3. MITRE ATT&CK technique
    4. Immediate response steps
    5. Real threat or false positive?

    ALERT: {json.dumps(alert, indent=2)}
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
def get_real_alerts(log_file="/home/saira/ai-soc-assistant/alerts.json", limit=5):
    """Read real alerts directly from Wazuh log file"""
    alerts = []
    try:
        with open(log_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        alert = json.loads(line)
                        alerts.append(alert)
                        if len(alerts) >= limit:
                            break
                    except json.JSONDecodeError:
                        continue
    except FileNotFoundError:
        print(f"❌ Log file not found: {log_file}")
    return alerts

print("🛡️  AI SOC ASSISTANT - REAL ALERTS")
print("=" * 60)

alerts = get_real_alerts()

if not alerts:
    print("❌ No alerts found!")
else:
    for i, alert in enumerate(alerts, 1):
        rule = alert.get('rule', {})
        agent = alert.get('agent', {})
        
        print(f"\n[ALERT {i}]")
        print(f"Rule: {rule.get('description', 'N/A')}")
        print(f"Severity: {rule.get('level', 'N/A')}")
        print(f"Agent: {agent.get('name', 'N/A')}")
        print("-" * 60)
        
        result = analyze_alert(alert)
        print(result)
        print("=" * 60)
