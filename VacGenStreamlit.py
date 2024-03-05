import streamlit as st
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

#Load the model and tokenizer
model_name = "Rijgersberg/GEITje-7B-chat-v2"  # Specify the name of your language model here
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelWithLMHead.from_pretrained(model_name)

from transformers import AutoModelForCausalLM, AutoTokenizer

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model_name = 'Rijgersberg/GEITje-7B-chat-v2'
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16,
                                             low_cpu_mem_usage=True, use_flash_attention_2=False,
                                             device_map=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def generate_text(input_text, style_text):
    # Combine input and style text
    input_style_text = input_text + " " + style_text

    # Tokenize the combined text
    input_ids = tokenizer.encode(input_style_text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate text based on the combined input and style
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, temperature=0.8)

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text



def main():
    with st.sidebar:
        st.title("Vacature generator v0.1")
        st.write("Selecteer de volgende items en klik dan op genereer")
        
        if st.button("Hoogleraar"):
            input_prompt = "Wat is de definitie van een hoogleraar?"
            input_text = "Wat is de definitie van een hoogleraar?"
            style_text = "Ik ben een hoogleraar in de informatica."
        option = st.selectbox('Om welke functie gaat het?',    ('Hoogleraar', 'IT manager', 'HR adviseur'))
        if st.button("Genereer!"):
            st.write("hello ik ben een vacature")

    # st.title("Language Model with Style Transfer")

    # Text input for the user
    input_text = st.text_area("Input Text", "Enter your text here...")

    # Style input for the user
    style_text = st.text_area("Style Text", "Enter your style text here...")




    # Button to generate text
    if st.button("Generate Text"):
        # Generate text based on the input and style texts
        # generated_text = generate_text(input_text, style_text)

        # Display the generated text
        st.subheader("Generated Text")
        # st.write(generated_text)


if __name__ == "__main__":
    main()
