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

    return jsonify({'generated_text': generated_texts})

if __name__ == '__main__':
    app.run(debug=True)