import openai
import os
import colorama

openai.api_key = "<YOUR_OPENAI_API_KEY>"
model_engine = "gpt-3.5-turbo"

while True:
    print("")
    prompt = input(colorama.Fore.YELLOW + "Ask Me Anything: " + colorama.Style.RESET_ALL)
    if prompt.lower() == "exit":
        break
    completion = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message['content']
    print(colorama.Fore.GREEN + response + colorama.Style.RESET_ALL, end='\n\n')
