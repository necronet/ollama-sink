from ollama import chat

stream = chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'Call a function to get weather in Miami'}],
    stream=True,
)

buffer = ''

for chunk in stream:
    if chunk.message.content:
        buffer += chunk.message.content

        # naive tool detection
        if "CALL_WEATHER_API" in buffer:
            print("\n⚡ Trigger tool call!\n")
