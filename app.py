 from flask import Flask
app = Flask(__name__)
ECO = "0776051066"
WA = "263776051066"

@app.route("/")
def home():
    html = """
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<style>
body{margin:0;font-family:Arial;background:#e8f5e9}
.top{background:#009739;color:#fff;text-align:center;padding:30px 10px;font-size:28px;font-weight:bold}
.wrap{width:100%}
.card{background:#fff;margin:15px;padding:25px;border-radius:15px}
input{width:100%;padding:18px;font-size:22px;border:2px solid #009739;border-radius:10px;margin:10px 0;box-sizing:border-box}
button{width:100%;padding:18px;background:#009739;color:#fff;border:none;border-radius:12px;font-size:20px;font-weight:bold}
.profit{font-size:36px;text-align:center;color:#009739;font-weight:bold;margin:15px 0}
.btn{display:block;padding:20px;border-radius:12px;text-align:center;text-decoration:none;font-weight:bold;font-size:19px;margin:15px}
</style></head><body>
<div class='top'>🇿🇼 Tuckshop Bot<br><span style='background:gold;color:black;padding:6px 18px;border-radius:20px;font-size:16px'>1 USD = 26.5 ZiG</span></div>
<div class='wrap'>
<div class='card'>
<h2 style='color:#009739;margin:0 0 10px'>Profit Calculator</h2>
Cost $<input id='c' type='number' value='10'>
Sell $<input id='s' type='number' value='15'>
<button onclick="document.getElementById('p').innerHTML='Profit $'+(document.getElementById('s').value-document.getElementById('c').value)">CALCULATE PROFIT</button>
<div id='p' class='profit'>Profit $5</div>
</div>
<a class='btn' style='background:#25D366;color:white' href='https://wa.me/263776051066?text=ADD me to group'>✅ JOIN FREE WHATSAPP GROUP<br><small>Harare Cheap Stock - 0776051066</small></a>
<div class='card'>
<h3>💰 Make More Money</h3>
<a class='btn' style='background:#eee;color:black' href='/suppliers'>🔍 Find Cheap Suppliers (Save 20%)</a>
<a class='btn' style='background:gold;color:black' href='/premium'>Unlock Premium - $5/month</a>
</div>
<div class='card' style='background:gold;border:3px solid black;text-align:center'>
<h2 style='margin:0'>📢 WHOLESALER? ADVERTISE $10!</h2>
<p>Get 100+ tuckshop owners daily!</p>
<a class='btn' style='background:#009739;color:white' href='https://wa.me/263776051066?text=I want to advertise $10'>ADVERTISE NOW - $10<br>EcoCash 0776051066</a>
</div>
<p style='text-align:center;color:gray;padding:20px'>Made in Harare ❤️<br>WhatsApp: 0776051066<br>EcoCash USD 0776051066</p>
</div></body></html>
"""
    return html

@app.route("/suppliers")
def suppliers():
    return "<h1>Suppliers page - coming soon</h1><a href='/'>Back Home</a>"

@app.route("/premium")
def premium():
    return "<h1>Premium $5 - EcoCash 0776051066</h1><a href='/'>Back Home</a>"

if __name__ == "__main__":
    app.run()
