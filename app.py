from flask import Flask
import requests, re, os
from datetime import datetime
app = Flask(__name__)

def get_rbz_rate():
    default_rate = 26.96
    try:
        r = requests.get("https://www.rbz.co.zw/index.php/reserve-bank-2/exchange-rates", timeout=6, headers={"User-Agent":"Mozilla/5.0"})
        m = re.search(r'USD[^0-9]*([2-3][0-9]\.\d{2,4})', r.text, re.I)
        if m:
            rate = float(m.group(1))
            if 20 < rate < 40: return rate
    except: pass
    return default_rate

GROUP_LINK = "https://chat.whatsapp.com/GPbgL4kcTyFLHoNuvdEkI9"

@app.route("/")
def home():
    rate = get_rbz_rate()
    today = datetime.now().strftime("%d %b %Y")
    return f"""<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{{margin:0;font-family:Arial;background:#e8f5e9}}.top{{background:#009739;color:#fff;text-align:center;padding:25px 10px;font-size:26px;font-weight:bold}}.card{{background:#fff;margin:12px;padding:20px;border-radius:15px}}input{{width:100%;padding:16px;font-size:20px;border:2px solid #009739;border-radius:10px;margin:8px 0;box-sizing:border-box}}button{{width:100%;padding:16px;background:#009739;color:#fff;border:none;border-radius:12px;font-size:18px;font-weight:bold}}.profit{{font-size:32px;text-align:center;color:#009739;font-weight:bold;margin:12px 0}}.btn{{display:block;padding:16px;border-radius:12px;text-align:center;text-decoration:none;font-weight:bold;font-size:17px;margin:12px}}</style>
    <script>const RATE={rate};function calc(){{let c=parseFloat(document.getElementById('c').value)||0;let s=parseFloat(document.getElementById('s').value)||0;let p=s-c;let perc=c>0?((p/c)*100).toFixed(1):0;document.getElementById('p').innerHTML='Profit $'+p.toFixed(2)+' ('+perc+'%)';document.getElementById('zig').innerHTML='ZiG Profit: '+(p*RATE).toFixed(2)+' ZiG';}}function usdToZig(){{let u=document.getElementById('u').value||0;document.getElementById('zout').innerHTML=(u*RATE).toFixed(2)+' ZiG';}}window.onload=calc;</script>
    </head><body><div class='top'>Tuckshop Bot PRO<br><span style='background:gold;color:black;padding:5px 15px;border-radius:20px;font-size:14px'>1 USD = {rate} ZiG - RBZ {today}</span></div>
    <div class='card'><h2 style='margin:0;color:#009739'>Profit Calculator</h2>Cost $<input id='c' type='number' value='10' oninput='calc()'>Sell $<input id='s' type='number' value='15' oninput='calc()'><button onclick='calc()'>CALCULATE</button><div id='p' class='profit'></div><div id='zig' style='text-align:center;background:gold;padding:10px;border-radius:10px;font-weight:bold'></div></div>
    <div class='card' style='background:#fff8e1;border:2px solid gold'><h3 style='margin:0'>USD to ZiG</h3>USD $<input id='u' type='number' value='1' oninput='usdToZig()'><button onclick='usdToZig()' style='background:gold;color:black'>CONVERT</button><div id='zout' class='profit'>{rate} ZiG</div></div>
    <a class='btn' style='background:#25D366;color:white' href='{GROUP_LINK}'>JOIN FREE WHATSAPP GROUP<br>Daily Cheap Stock</a>
    <div class='card' style='background:gold;border:3px solid black;text-align:center'><h2 style='margin:0'>WHOLESALER? ADVERTISE $10!</h2><p>100+ owners see you DAILY!</p><a class='btn' style='background:#009739;color:white' href='{GROUP_LINK}'>ADVERTISE NOW<br>Chat on WhatsApp Only</a></div>
    <p style='text-align:center;color:gray;padding:15px'>Made in Harare - Tuckshop Bot<br>RBZ Official: {rate}</p></body></html>"""

if __name__=="__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
