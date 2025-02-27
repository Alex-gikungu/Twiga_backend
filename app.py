# app.py
from flask import Flask
from flask_cors import CORS  # Import CORS
from models import db
from routes import init_mail, register_routes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Initialize mail and register routes
init_mail(app)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)