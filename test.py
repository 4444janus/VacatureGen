
from tqdm import tqdm, trange

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

#AI stuff
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_name = 'Rijgersberg/GEITje-7B-chat-v2'
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16,
                                             low_cpu_mem_usage=True, use_flash_attention_2=False,
                                             device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate(prompt, temperature=0.2, top_k=50, max_new_tokens=1_000):
    conversation = [
    {
        'role': 'user',
        'content': prompt
    }
    ]

    tokenized = tokenizer.apply_chat_template(conversation, add_generation_prompt=True,
                                              return_tensors='pt').to(device)
    outputs = model.generate(tokenized, do_sample=True, temperature=temperature,
                             top_k=top_k, max_new_tokens=max_new_tokens)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)