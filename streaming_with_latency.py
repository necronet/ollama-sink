import time
from ollama import chat

start = time.time()

stream = chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'Given this [1,5,10,2,30,200,100,200,30] get me the following statistics like mean, mode, median and standard deviation in a nice table in markdown'}],
    stream=True,
)

first_token_time = None

for chunk in stream:
    if chunk.message.content:
        if first_token_time is None:
            first_token_time = time.time()
            print(f"\n⏱️ Time to first token: {first_token_time - start:.2f}s\n")

        print(chunk.message.content, end='', flush=True)

end = time.time()
print(f"\n\n✅ Total time: {end - start:.2f}s")
