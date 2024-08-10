from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("path/to/llama3")
model = AutoModelForCausalLM.from_pretrained("path/to/llama3")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    temperatures = data.get('temperatures', {})

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors='pt')

    # Generate text with different temperatures for each agent
    generated_texts = {}
    for agent, temperature in temperatures.items():
        with torch.no_grad():
            outputs = model.generate(inputs['input_ids'], max_length=100, temperature=temperature)
        generated_texts[agent] = tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)