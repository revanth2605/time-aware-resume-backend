from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from routes.dashboard_routes import dashboard_bp
from routes.upload_routes import upload_bp
from routes.resume_routes import resume_bp
from routes.public_routes import public_bp
from routes.search_routes import search_bp
from routes.auth_routes import auth_bp
from routes.register_routes import register_bp


app = Flask(__name__)
CORS(app)

# 🔐 JWT Configuration
import os
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600  # 1 hour

jwt = JWTManager(app)

# Register routes
app.register_blueprint(dashboard_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(public_bp)
app.register_blueprint(search_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(register_bp)

@app.route("/")
def home():
    return "Time-Aware Resume Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

