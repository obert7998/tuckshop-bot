from flask import Flask, request
app = Flask(__name__)

# --- YOUR PAYMENT DETAILS - CHANGE THESE ---
ECOCASH_NUMBER = "0771234567"  # <--- Put your EcoCash here
WHATSAPP_NUMBER = "263771234567" # <--- Your WhatsApp

@app.route("/")
def home():
    return """
    <body style='margin:0;font-family:Arial;background:#f0fff0'>
    <div style='background:#009739;color:white;padding:20px;text-align:center'>
    <h1>🇿🇼 Tuckshop Bot</h1>
    <div style='background:gold;color:black;padding:8px 20px;border-radius:20px;display:inline-block'>1 USD = 26.5 ZiG</div>
    </div>
    <div style='padding:20px;max-width:380px;margin:auto'>
    
    <div style='background:white;padding:20px;border-radius:15px;box-shadow:0 2px 10px #ccc'>
    <h2 style='color:#009739'>Profit Calculator</h2>
    <form>
    Cost $: <input type='number' id='c' value='10' style='width:60px;padding:8px'><br><br>
    Sell $: <input type='number' id='s' value='15' style='width:60px;padding:8px'><br><br>
    <button type='button' onclick="document.getElementById('p').innerHTML='Profit: $'+(s.value-c.value)" style='padding:10px 20px;background:#009739;color:white;border:none;border-radius:8px'>Calculate</button>
    <div id='p' style='font-size:28px;color:#009739;font-weight:bold;margin-top:15px'>Profit $5</div>
    </form>
    </div>

    <div style='background:white;padding:20px;border-radius:15px;margin-top:20px;box-shadow:0 2px 10px #ccc'>
    <h3>💰 Make More Money</h3>
    <a href='/suppliers' style='display:block;padding:12px;background:#009739;color:white;text-align:center;text-decoration:none;border-radius:8px;margin-bottom:10px'>🏪 Find Cheap Suppliers (Save 20%)</a>
    <a href='/premium' style='display:block;padding:12px;background:gold;color:black;text-align:center;text-decoration:none;border-radius:8px;font-weight:bold'>⭐ Unlock Premium - $5/month</a>
    </div>

    <p style='text-align:center;color:gray;margin-top:20px'>Made in Harare ❤️ | <a href='/suppliers'>Advertise Your Wholesale Here</a></p>
    </div>
    </body>
    """

@app.route("/suppliers")
def suppliers():
    return f"""
    <body style='margin:0;font-family:Arial;background:#f0fff0'>
    <div style='padding:20px;max-width:380px;margin:auto'>
    <a href='/'><- Back</a>
    <h2>🏪 Wholesale Suppliers - Harare</h2>
    
    <div style='background:white;padding:15px;border-radius:10px;margin-bottom:15px;border-left:5px solid #009739'>
    <b>Gain Cash & Carry - Graniteside</b><br>Best for: Sugar, Flour, Oil<br>
    <a href='https://wa.me/{WHATSAPP_NUMBER}?text=I want Gain supplier' style='color:#009739'>Order via Tuckshop Bot (You save 2%)</a><br>
    <small style='color:gray'>Ad - Pay $10/month to be here</small>
    </div>

    <div style='background:white;padding:15px;border-radius:10px;margin-bottom:15px;border-left:5px solid gold'>
    <b>Mohammed Mussa - Gulf Complex</b><br>Best for: Sweets, Biscuits, $1 deals<br>
    <a href='https://wa.me/{WHATSAPP_NUMBER}' style='color:#009739'>Contact</a><br>
    <small style='color:gray'>Ad - Pay $10/month to be here</small>
    </div>

    <div style='background:gold;padding:15px;border-radius:10px;text-align:center'>
    <h3>Are you a wholesaler?</h3>
    <p>Get 100+ tuckshop owners to see you daily</p>
    <a href='https://wa.me/{WHATSAPP_NUMBER}?text=I want to advertise my wholesale for $10' style='display:block;padding:12px;background:#009739;color:white;text-decoration:none;border-radius:8px'>Advertise for $10/month - WhatsApp Us</a>
    </div>
    </div>
    </body>
    """

@app.route("/premium")
def premium():
    return f"""
    <body style='margin:0;font-family:Arial;background:#f0fff0'>
    <div style='padding:20px;max-width:380px;margin:auto'>
    <a href='/'><- Back</a>
    <h2>⭐ Premium - $5/month</h2>
    <div style='background:white;padding:20px;border-radius:15px'>
    <p>✅ Stock Management</p>
    <p>✅ Daily Profit Reports via WhatsApp</p>
    <p>✅ Low Stock Alerts</p>
    <p>✅ Supplier Price Comparison</p>
    <hr>
    <h3>Pay with EcoCash:</h3>
    <p style='font-size:20px;background:#ff8c00;color:white;padding:15px;border-radius:10px;text-align:center'>EcoCash: {ECOCASH_NUMBER}<br>Amount: $5</p>
    <a href='https://wa.me/{WHATSAPP_NUMBER}?text=I paid $5 EcoCash for Premium' style='display:block;padding:15px;background:#25D366;color:white;text-align:center;text-decoration:none;border-radius:10px;font-weight:bold'>I Paid - Send Proof on WhatsApp</a>
    <p style='text-align:center;margin-top:15px'><small>After you send proof, we activate you in 5 mins</small></p>
    </div>
    </div>
    </body>
    """

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
