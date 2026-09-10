 from flask import Flask
import requests, re
from datetime import datetime

app = Flask(__name__)

def get_rbz_rate():
    # Default - from RBZ news Sept 2026
    default_rate = 26.96
    try:
        # Try fetch RBZ page
        r = requests.get("https://www.rbz.co.zw/index.php/reserve-bank-2/exchange-rates", timeout=6, headers={"User-Agent":"Mozilla/5.0"})
        text = r.text
        # Look for USD = ZiG pattern - RBZ table has USD 26.xx
        # Search for 26.xxx or 27.xxx
        match = re.search(r'USD[^0-9]*([2-3][0-9]\.\d{2,4})', text, re.I)
        if match:
            rate = float(match.group(1))
            if 20 < rate < 40: # sanity check for ZiG
                return rate
        # Fallback parse any 26-27 value near ZWG
        match2 = re.search(r'ZWG\s*26\.\d+|26\.\d+\s*ZWG|ZiG\s*26\.\d+', text, re.I)
        if match2:
            num = re.search(r'26\.\d+', match2.group(0))
            if num:
                return float(num.group(0))
    except:
        pass
    return default_rate

@app.route("/")
def home():
    rate = get_rbz_rate()
    today = datetime.now().strftime("%d %b %Y")
    return f"""<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{{margin:0;font-family:Arial;background:#e8f5e9}}.top{{background:#009739;color:#fff;text-align:center;padding:25px 10px;font-size:26px;font-weight:bold}}.card{{background:#fff;margin:12px;padding:20px;border-radius:15px}}input{{width:100%;padding:16px;font-size:20px;border:2px solid #009739;border-radius:10px;margin:8px 0;box-sizing:border-box}}button{{width:100%;padding:16px;background:#009739;color:#fff;border:none;border-radius:12px;font-size:18px;font-weight:bold}}.profit{{font-size:32px;text-align:center;color:#009739;font-weight:bold;margin:12px 0}}.btn{{display:block;padding:16px;border-radius:12px;text-align:center;text-decoration:none;font-weight:bold;font-size:17px;margin:12px}}.zig{{background:#fff8e1;border:2px solid gold}}</style><script>
    const RATE={rate};
    function calc(){{let c=parseFloat(document.getElementById('c').value)||0;let s=parseFloat(document.getElementById('s').value)||0;let p=s-c;let perc=c>0?((p/c)*100).toFixed(1):0;document.getElementById('p').innerHTML='Profit $'+p+' ('+perc+'%)';document.getElementById('zig').innerHTML='ZiG Profit: '+(p*RATE).toFixed(2)+' ZiG<br>Sell: '+(s*RATE).toFixed(2)+' ZiG';}}
    function usdToZig(){{let u=document.getElementById('u').value||0;document.getElementById('zout').innerHTML=(u*RATE).toFixed(2)+' ZiG';}}
    </script></head><body><div class='top'>Tuckshop Bot PRO<br><span style='background:gold;color:black;padding:5px 15px;border-radius:20px;font-size:14px'>1 USD = {rate} ZiG - RBZ {today}</span></div><div class='card'><h2 style='color:#009739;margin:0'>Profit Calculator</h2>Cost $<input id='c' type='number' value='10' oninput='calc()'>Sell $<input id='s' type='number' value='15' oninput='calc()'><button onclick='calc()'>CALCULATE PROFIT</button><div id='p' class='profit'>Profit $5 (50%)</div><div id='zig' style='text-align:center;background:gold;padding:10px;border-radius:10px;font-weight:bold'>ZiG Profit: 132.5 ZiG<br>Sell: 397.5 ZiG</div></div><div class='card zig'><h3 style='margin:0'>USD to ZiG Converter</h3>USD $<input id='u' type='number' value='1' oninput='usdToZig()'><button onclick='usdToZig()' style='background:gold;color:black'>CONVERT TO ZiG</button><div id='zout' class='profit' style='font-size:28px'>{rate} ZiG</div></div><a class='btn' style='background:#25D366;color:white' href='https://wa.me/263776051066?text=ADD%20me%20to%20Daily%20Cheap%20Stock'>JOIN FREE WHATSAPP GROUP<br>Daily Cheap Stock</a><div class='card' style='background:gold;border:3px solid black;text-align:center'><h2 style='margin:0'>WHOLESALER? ADVERTISE $10!</h2><p>100+ owners see you DAILY!</p><a class='btn' style='background:#009739;color:white' href='https://wa.me/263776051066?text=Hi%20I%20want%20to%20ADVERTISE%20$10%20on%20Tuckshop%20Bot'>ADVERTISE NOW<br>Chat on WhatsApp Only</a></div><p style='text-align:center;color:gray;padding:15px'>RBZ Official Rate: {rate} - Made in Harare</p></body></html>"""

@app.route("/rate")
def rate_api():
    return {"rbz_rate": get_rbz_rate(), "source": "RBZ official", "date": datetime.now().isoformat()}

@app.route("/suppliers")
def s(): return "<h1>Suppliers Coming Soon</h1><p>Chat us on WhatsApp</p><a href='/'>Back</a>"
@app.route("/premium")
def p(): return "<h1>Premium $5</h1><p>Chat us on WhatsApp to upgrade</p><a href='https://wa.me/263776051066?text=Premium'>Upgrade</a><br><a href='/'>Back</a>"
if __name__=="__main__": app.run()
