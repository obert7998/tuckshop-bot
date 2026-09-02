 from flask import Flask, request
app = Flask(__name__)

ECOCASH_NUMBER = "0776051066"
WHATSAPP_NUMBER = "263776051066"

@app.route("/")
def home():
    return f"""
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
    *{{box-sizing:border-box}} 
    body{{margin:0;font-family:Arial;background:#f0fff0;min-height:100vh}}
    .header{{background:#009739;color:white;text-align:center;padding:25px 15px}}
    .header h1{{margin:0;font-size:32px}} 
    .content{{width:100%;max-width:600px;margin:0 auto;padding:15px}}
    .card{{background:white;padding:25px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.1);margin-bottom:20px;width:100%}}
    input{{width:100%;padding:15px;margin:10px 0;border:2px solid #009739;border-radius:10px;font-size:20px}}
    button{{background:#009739;color:white;border:none;padding:16px;border-radius:10px;font-weight:bold;font-size:18px;width:100%;margin-top:10px}}
    #p{{font-size:32px;color:#009739;font-weight:bold;text-align:center;margin-top:15px}}
    </style></head>
    <body>
    <div class='header'>
    <h1>🇿🇼 Tuckshop Bot</h1>
    <div style='background:gold;color:black;padding:8px 20px;border-radius:20px;display:inline-block;margin-top:10px;font-size:16px'>1 USD = 26.5 ZiG</div>
    </div>
    
    <div class='content'>
    <div class='card'>
    <h2 style='color:#009739;margin-top:0'>Profit Calculator</h2>
    <form>
    Cost $: <input type='number' id='c' value='10'>
    Sell $: <input type='number' id='s' value='15'>
    <button type='button' onclick="document.getElementById('p').innerHTML='Profit $'+(document.getElementById('s').value-document.getElementById('c').value)">Calculate Profit</button>
    <div id='p'>Profit $5</div>
    </form>
    </div>

    <div class='card' style='background:#25D366;text-align:center'>
    <a href='https://wa.me/{WHATSAPP_NUMBER}?text=ADD me to Harare Cheap Stock' style='color:white;text-decoration:none;font-weight:bold;font-size:18px;display:block'>✅ JOIN FREE WHATSAPP GROUP - HARARE CHEAP STOCK</a>
    <p style='color:white;margin:5px 0 0;font-size:14px'>Daily deals - Sugar, Flour, Oil - 0776051066</p>
    </div>

    <div class='card'>
    <h3>💰 Make More Money</h3>
    <a href='/suppliers' style='display:block;padding:15px;background:#f0f0f0;border-radius:10px;text-decoration:none;color:black;margin-bottom:10px;font-size:16px'>🔍 Find Cheap Suppliers (Save 20%)</a>
    <a href='/premium' style='display:block;padding:15px;background:gold;border-radius:10px;text-decoration:none;color:black;font-weight:bold;text-align:center;font-size:16px'>Unlock Premium - $5/month</a>
    </div>

    <div class='card' style='background:gold;text-align:center;border:3px solid #000'>
    <h3 style='margin:0;color:#000'>📢 WHOLESALER? ADVERTISE FOR $10!</h3>
    <p style='margin:5px 0'>Get 100+ tuckshop owners daily!</p>
    <a href='https://wa.me/{WHATSAPP_NUMBER}?text=I want to ADVERTISE for $10' style='display:block;background:#009739;color:white;padding:15px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:18px;margin-top:10px'>ADVERTISE NOW - $10 - EcoCash<br>{ECOCASH_NUMBER}</a>
    </div>

    <p style='text-align:center;color:gray;padding:20px'>Made in Harare ❤️ | WhatsApp: 0776051066<br>EcoCash USD {ECOCASH_NUMBER}</p>
    </div></body></html>
    """

@app.route("/suppliers")
def suppliers():
    return f"<h1>Suppliers - WhatsApp {ECOCASH_NUMBER}</h1><a href='/'>Back</a>"

@app.route("/premium")
def premium():
    return f"<h1>Premium $5 - EcoCash {ECOCASH_NUMBER}</h1><a href='https://wa.me/{WHATSAPP_NUMBER}'>Pay Now</a><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run()
