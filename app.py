from flask import Flask
from routes.auth_routes import auth_bp
from routes.emotion_routes import emotion_bp
from routes.home_routes import home_bp
from utils.supabase_client import supabase

app = Flask(__name__)
app.secret_key = "your-secret-key"

# Register Blueprints (modular routes)
app.register_blueprint(auth_bp)
app.register_blueprint(emotion_bp)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(debug=True)
