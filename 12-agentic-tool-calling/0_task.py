from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="Hello, world!",
    model="o3-mini",
    background=True,
)

print(response)
