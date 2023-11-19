
from flask import Flask, render_template, request
import pprint
import google.generativeai as palm
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.j2")

@app.route('/askdog', methods = ["POST", "GET"])
def AskDog():
    
    if request.method == "GET":
        return render_template("ask_dog.j2")
    
    if request.method == "POST":
        if request.form.get("question"):
            question = request.form["question"]
            
            palm.configure(api_key=os.environ["PALM_KEY"])

            models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
            model = models[0].name

            # prompt = At the end, make a joke about dogs being better than cats starting with
            # "You're probably also wondering why dogs are better than cats:"

            prompt_lead = """Answer all questions starting with "WOOF". 
            Then tell the story like a dog would. 
            """

            prompt = prompt_lead + " " + question

            completion = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=0,
                # The maximum length of the response
                max_output_tokens=800,
            )

            results = completion.result
            
            if results is None:
                results = "Hmmm, I'm not so great with knowing facts, I could tell you a story though! WOOF!"
            
            # print(completion.result)
            return render_template("ask_dog.j2", results=results, prompt=question)

@app.route('/chatdog')
def chatdog():
    return render_template("chat_dog.j2")

if __name__ == '__main__':
    app.run()
