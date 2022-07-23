#### Important
Automation for gmail is now prohibited from google. This acts as an illustration of how to interact with web elements using Selenium in Python.

The project is setup using page object model design pattern.
- We have pages folder where we list the methods for how to interact with pages
- We have locators file in utils folder, where we list the locators of web elements

### Note
This guide is for Linux base machine
Windows or Mac is a little bit diffrent in setup when it comes to PATH and virtualenv setup
### 1. Add chromedriver to PATH
- Download chromedriver from google chrome driver
- Extract chromdriver zip file and add it to PATH

### 2. Add .env file to home folder of end to end test

### 3. Init virtualenv
virtualenv venv

### 4. Activate virtualenv
source venv/bin/activate 

### 5. Install dependencies
pip install -r requirements.txt

### 6. Run the test
pytest tests/test_send_email.py

