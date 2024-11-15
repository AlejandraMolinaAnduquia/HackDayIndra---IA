from transformers import AutoTokenizer, AutoModelForCausalLM

def initialize_chatbot():
    model_name = "mistral-large-latest"  # Cambia según tu modelo
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return {"tokenizer": tokenizer, "model": model}
