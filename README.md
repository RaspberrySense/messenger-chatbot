# Facebook Messenger chatbot
Facebook Messenger chatbot for Raspberry Sense.

## Setup
1. Create a Python 3 virtual environment, say `venv`.
1. Activate `venv` and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
1. Create `secrets.py` and add the following variables with their proper values:
   * `FACEBOOK_VERIFY_TOKEN`
   * `PAGE_ACCESS_TOKEN`
1. Set the `FLASK_APP` environment variable to `app.py`:
   ```bash
   export FLASK_APP=app.py
   ```
1. Run the app:
   ```bash
   flask run
   ```
