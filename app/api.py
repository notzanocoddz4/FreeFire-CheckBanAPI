from flask import Flask
from app.routes.checkbanned import checkbanned_bp

app = Flask(__name__)

app.register_blueprint(checkbanned_bp)

@app.route('/')
def home():
    return {
        "status": "online",
        "message": "Free Fire CheckBanAPI has been running (made by notzanocoddz)"
    }