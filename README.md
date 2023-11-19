# ChatterDog

### Live Deployment - https://chatterdog-y6wtdz7vwq-ue.a.run.app/

## What is it?

Welcome to ChatterDog! Chatterdog is a web application that allows users the ability to ask a highly intelligent dog a question.

## How does it work?

Chatterdog is a Flask application enabled via the PaLM API from Google and deployed using Google Cloud Run. It consumes user inputs and responds accordingly. The model has been tuned to respond as a dog would.

## Why build it?

For fun! ChatterDog was built as part of the GoogleHacks Hackathon at Oregon State University which required the use of at least one Google technology and the idea sprouted from always spending time with my own dog and imagining how she'd respond to questions if she could. 

It gave me a chance to explore building a Flask app while connecting to external APIs and also explore using Google PaLM for the first time. This was my first time utilizing Google PaLM or any other AI service as a developer and it was fun to experiment with methods to influence output and also learn how to address some of the common errors I encountered (rejected responses to factual asks etc.)

## Developer Notes
1. The app was developed using [pipenv](https://pipenv.pypa.io/en/latest/) to manage packages in the virtual environment. A requirements.txt file was generated using `pipenv run pip freeze > requirements.txt` to support deployment with Google Cloud Run.
2. The `main.py` file is a requirement of a basic Google Cloud Run deployment and simply routes to and runs `app.py`
3. For local development, a `.env` file with the `PALM_KEY` variable defined is necessary.
4. To deploy using Google Cloud Run you must [set the environment variable](https://cloud.google.com/run/docs/configuring/services/environment-variables) to be used in the deployment as well.

## Relevant Links

- Google PaLM API Docs - https://developers.generativeai.google/tutorials/text_quickstart
- Google Cloud Run Docs - https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
- Flask Docs - https://flask.palletsprojects.com/en/2.3.x/quickstart/

