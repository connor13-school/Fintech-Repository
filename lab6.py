
#import os
#from dotenv import load_dotenv
from openai import OpenAI

openai_model = 'gpt-4o-mini' 
#load_dotenv()  
#api_key = os.getenv('OPENAI_API_KEY')
api_key = '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'
client = OpenAI(api_key = api_key) 



user_content = "What are TCU's official colors?" # <-------------- Change this
#system_content = "Chatbot role"
temperature = 0


message = [{"role": "user", "content": user_content}, 
#           {"role": "system", "content": system_content}
           ]


chat_completion = client.chat.completions.create(
    messages=message,
    temperature=temperature,
    model=openai_model
)


print(chat_completion.choices[0].message.content)