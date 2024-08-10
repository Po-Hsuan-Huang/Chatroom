from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import random
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatroom.db'
db = SQLAlchemy(app)

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("path/to/llama3")
model = AutoModelForCausalLM.from_pretrained("path/to/llama3")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_photo = db.Column(db.String(200), nullable=True)  # Add profile photo URL

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    sender = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).limit(50).all()
    return jsonify([
        {
            'id': message.id,
            'content': message.content,
            'sender': message.sender,
            'timestamp': message.timestamp.isoformat()
        } for message in messages
    ])

@app.route('/messages', methods=['POST'])
def post_message():
    data = request.json
    new_message = Message(content=data['content'], sender=data['sender'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'status': 'success'}), 201

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'status': 'error', 'message': 'Username already exists'}), 400

    profile_photo = data.get('profile_photo')
    if not profile_photo:
        # Assign an unused photo if the user doesn't upload one
        profile_photos = [
            "static/images/11.png",
            "static/images/16.png",
            "static/images/17.png",
            "static/images/18.png",
            "static/images/19.png"
        ]
        used_photos = {user.profile_photo for user in User.query.all()}
        available_photos = [photo for photo in profile_photos if photo not in used_photos]
        if available_photos:
            profile_photo = random.choice(available_photos)
        else:
            profile_photo = "static/images/default.png"  # Fallback to a default photo if all are used

    new_user = User(username=data['username'], profile_photo=profile_photo)
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'success'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 400

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors='pt')

    # Generate text
    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], max_length=100)

    # Decode the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)