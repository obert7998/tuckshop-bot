from flask import Flask, request
import requests

app = Flask(__name__)

try:
    r = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=10)
    RATE = r.json()["rates"]["ZWG"]
except:
    RATE = 26.5

@app.route("/")
def home():
    cost = request.args.get("cost", "10")
    sell = request.args.get("sell", "15")
    try:
        cost = float(cost)
        sell = float(sell)
        profit = sell - cost
        need = cost * RATE * 1.2
        return f"""
        <h2>🇿🇼 Tuckshop Bot - Rate 1 USD = {RATE} ZiG</h2>
        <p>Cost: ${cost} | Sell: ${sell}</p>
        <h3>Profit: ${profit} ({profit*RATE:.2f} ZiG)</h3>
        <p>For 20% profit charge: {need:.2f} ZiG</p>
        <p>Try: /?cost=20&sell=35</p>
        <form>
          Cost: <input name=cost> Sell: <input name=sell> <button>Calculate</button>
        </form>
        """
    except:
        return "Use /?cost=10&sell=15"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
