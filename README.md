# ChatterDog

### Live Deployment - https://chatterdog-y6wtdz7vwq-ue.a.run.app/

## Inspiration

ChatterDog was built as part of the GoogleHacks Hackathon at Oregon State University which required the use of at least one Google technology and the idea sprouted from always spending time with my own dog and imagining how she'd respond to questions if she could. 

It gave me a chance to explore building a Flask app while connecting to external APIs and also experiment using Google PaLM for the first time. This was my first time utilizing Google PaLM or any other AI service as a developer and it was fun to experiment with methods to influence output and also learn how to address some of the common errors I encountered (rejected responses to factual asks etc.). I also hadn't used Google Cloud Run previously and found it very simple to deploy with after experimenting with other dynamic site deployment methods.

## What it does

ChatterDog is a web application that allows users the ability to ask a highly intelligent dog the toughest of questions or just ask for Dog's input based on a wealth of experience.

## How I built it

ChatterDog is a Flask application enabled via the PaLM API from Google and deployed using Google Cloud Run. It consumes user inputs and responds accordingly. The model has been tuned to respond as a dog would.

## Challenges we ran into

Apart from just general learning of new technologies and basic syntax errors and debugging the biggest challenge was deploying using Google Cloud Run. To deploy using Google Cloud Run you must [set the environment variable](https://cloud.google.com/run/docs/configuring/services/environment-variables) to be used in the deployment as well (this is overlooked in the introductory documentation and took me some time to troubleshoot the reason my app didn't function properly when deployed vs. locally run)

## Accomplishments that I'm proud of

This was my first time building a Flask app that accesses an external API (I've only connected to SQL DBs using Flask previously). Further, this was my first time utilizing Google PaLM or any other AI service as a developer and it was fun to experiment with methods to influence output and also learn how to address some of the common errors I encountered (rejected responses to factual asks etc.). I also hadn't used Google Cloud Run previously and found it very simple to deploy with after experimenting with other dynamic site deployment methods.

## What I learned

I learned I really like using Flask for backend development but resources for frontend work are much more limited than some other frameworks (at least for my experience). If I were to build this again I would look into building with Node.js and React to increase flexibility in my frontend development. I also learned that Google Cloud Run as a deploy method is preferable for dynamic site deployment over Google App Engine which was my first attempted deploy method.

## What's next for ChatterDog

I'd like to expand this to have the ability to ask a cat questions and also introduce chat functionality so you could have a running conversation with a dog. Currently the app doesn't remember past responses but continuous chat functionality would have the Dog remember past interactions in the conversation and respond accordingly.

## Developer Notes
1. The app was developed using [pipenv](https://pipenv.pypa.io/en/latest/) to manage packages in the virtual environment. A requirements.txt file was generated using `pipenv run pip freeze > requirements.txt` to support deployment with Google Cloud Run.
2. The `main.py` file is a requirement of a basic Google Cloud Run deployment and simply routes to and runs `app.py`
3. For local development, a `.env` file with the `PALM_KEY` variable defined is necessary.
4. To deploy using Google Cloud Run you must [set the environment variable](https://cloud.google.com/run/docs/configuring/services/environment-variables) to be used in the deployment as well (this is overlooked in the introductory documentation and took me some time to troubleshoot the reason my app didn't function properly when deployed vs. locally run)

## Relevant Links

- Google PaLM API Docs - https://developers.generativeai.google/tutorials/text_quickstart
- Google Cloud Run Docs - https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
- Flask Docs - https://flask.palletsprojects.com/en/2.3.x/quickstart/

