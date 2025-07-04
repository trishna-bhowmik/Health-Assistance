from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from auth.models import db, bcrypt
from auth.routes import auth_bp
from intents.classifier import classify_intent
from intents.responses import get_response

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
bcrypt.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route('/ask', methods=['POST'])
def ask():
    from flask import request, jsonify
    data = request.get_json()
    question = data.get('question', '')
    intent = classify_intent(question)
    answer = get_response(intent, question)
    return jsonify({'intent': intent, 'answer': answer})

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
