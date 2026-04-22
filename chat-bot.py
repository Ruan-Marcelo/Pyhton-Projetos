from openai import OpenAI

endpoint = "endpoint"
deployment_name = "gpt-4o"
api_key = "suaKeyAqui"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "Quantos gols tem neymar?",
        }
    ],
)

print(completion.choices[0].message)