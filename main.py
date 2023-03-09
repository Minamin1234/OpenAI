import openai

with open("token.txt", "r") as f:
    API_KEY = f.readline()
    pass

openai.api_key = API_KEY

STOP = "stop"
EXIT = "exit"
QUIT = "quit"

logs: list[dict[str, str]] = [
    {"role": "system", "content": "ようこそ！"},
]

while True:
    line = str(input("user: "))
    if line == STOP or\
        line == EXIT or\
            line == QUIT:
        break
    logs.append(
        {"role": "user", "content": line}
    )
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=logs
    )
    result = res["choices"][0]["message"]["content"]
    print(f"AI: {result}")
    pass
