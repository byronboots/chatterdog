
import pprint
import google.generativeai as palm
import os

def AskDog():
    palm.configure(api_key=os.environ["PALM_KEY"])

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)

    # prompt = At the end, make a joke about dogs being better than cats starting with
    # "You're probably also wondering why dogs are better than cats:"

    prompt_lead = """Answer all questions starting with "WOOF". 
    Then answer the question intelligently while acting like a dog. 
    """

    prompt_input = input("Please ask the dog a question: ")

    prompt = prompt_lead + " " + prompt_input

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    print(completion.result)
    
print(AskDog())