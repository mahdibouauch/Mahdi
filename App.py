from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if 'سلام' in incoming_msg:
        msg.body('وعليكم السلام أ مهدي 🔥 الروبو ديالك خدام!')
    elif 'شحال' in incoming_msg:
        msg.body('أنا روبو مجاني خدام 24/7 أ البطل 💎')
    else:
        msg.body('أنا الروبو ديال مهدي 🤖 كتب سلام ولا شحال')
    
    return str(resp)

if __name__ == "__main__":
    app.run()
