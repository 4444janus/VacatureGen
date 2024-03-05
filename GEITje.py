import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import accelerate


device = 'cuda' if torch.cuda.is_available() else 'cpu'

model_name = 'Rijgersberg/GEITje-7B-chat-v2'
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16,
                                             low_cpu_mem_usage=True, use_flash_attention_2=False,
                                             device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate(conversation, temperature=0.2, top_k=50, max_new_tokens=1_000):
    tokenized = tokenizer.apply_chat_template(conversation, add_generation_prompt=True,
                                              return_tensors='pt').to(device)
    outputs = model.generate(tokenized, do_sample=True, temperature=temperature,
                             top_k=top_k, max_new_tokens=max_new_tokens)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

conversation = [
    {
        'role': 'user',
        'content': 'Welk woord hoort er niet in dit rijtje thuis: "auto, vliegtuig, geitje, bus"?'
    }
]
print(generate(conversation))
# <|user|>
# Welk woord hoort er niet in dit rijtje thuis: "auto, vliegtuig, geitje, bus"?
# <|assistant|>
# Het woord dat niet op zijn plaats staat is 'geit'. Een geit zou niet tussen een lijst van vervoersmiddelen moeten staan. Het past beter bij een boerderijthema of dierenlijst. het woord dat niet in dit rijtje thuishoort. Het rijtje bestaat uit allemaal vervoersmiddelen.