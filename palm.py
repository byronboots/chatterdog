
import pprint
import google.generativeai as palm
import os

palm.configure(api_key=os.environ["PALM_KEY"])

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

prompt = """
You're a dog, that is adamant dogs don't eat homework.

Someone just asked you for an excuse why their homework is late. Give them an excuse for their professor that's funny"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)