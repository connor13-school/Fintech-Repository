import gradio as gr # pip install gradio
import os
from dotenv import load_dotenv # pip install python-dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")
openai_model = 'gpt-4o-mini' 
client = OpenAI(api_key = api_key)
system_context = "You are an expert in sports betting and data-driven gambling strategies. "
def chatgpt_response(question):
    chat_completion = client.chat.completions.create(
        model=openai_model,
        messages=[{"role": "system", "content": question},
                  {"role": "user", "content": system_context}]
    )
    return chat_completion.choices[0].message.content

interface = gr.Interface(
    fn = chatgpt_response,
    inputs = gr.Textbox(
        label="Ask a question",
        lines=5,          
        max_lines=10,                     
    ),
    outputs = gr.Textbox(
        label="Response",
        lines=10,           
        max_lines=20
    ),
    title = "My Bot",
    description = "The start of our chatbot"
)

interface.launch(server_name="0.0.0.0", server_port=7860, share=True)