# Facebook Messenger chatbot
Facebook Messenger chatbot for Raspberry Sense.

## Setup
1. Create a Python 3 virtual environment, say `venv`.
1. Activate `venv` and install requirements:
   ```
   pip install -r requirements.txt
   ```
1. Create `secrets.py` and add the `PAGE_ACCESS_TOKEN` to it.
1. Set the `FLASK_APP` environment variable to `app.py`, the Flask app to be run:
   ```
   export FLASK_APP=app.py
   ```
1. Run the app:
   ```
   flask run
   ```
