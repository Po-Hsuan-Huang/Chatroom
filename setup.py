import os
import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer

def install_requirements():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

def download_llama3_model():
    cwd = os.getcwd()
    model_dir = os.path.join(cwd, "model", "llama3")
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    print("Cloning LLaMA 3 model repository...")
    subprocess.check_call(["git", "clone", "https://github.com/facebookresearch/llama3.git", model_dir])
    
    print("Downloading LLaMA 3 model...")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir)
    
    tokenizer.save_pretrained(model_dir)
    model.save_pretrained(model_dir)
    print("Model downloaded and saved to 'model/llama3' directory.")

if __name__ == "__main__":
    install_requirements()
    download_llama3_model()