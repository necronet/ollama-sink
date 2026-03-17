from ollama import chat

stream = chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'Explicame lo que es un API en 3 parrafos o menos'}],
    stream=True,
)

for chunk in stream:
    if chunk.message.content:
        print(chunk.message.content, end='', flush=True)
