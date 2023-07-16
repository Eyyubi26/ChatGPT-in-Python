import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

model_engine = "text-davinci-003"
prompt = input('Your question: ')

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=1,
)

response = completion.choices[0].text
print("AI:"+response)
