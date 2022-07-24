Unable to start the vsee application using

```
desired_caps = {
    "deviceName": "BKW00043349",
    "platformName": "Android",
    "version" : "11",
    "appPackage": "com.vsee.vsee.beta",
    "appActivity":"com.vsee.vsee.beta.MainActivity",
    "automationName":"Appium"

}
```
So I use "TheCofeeHouse" application instead for demonstration

# Scenario
- Open the "TheCoffeeHouse" application
- Assert the text "Chao ban moi" is displayed
- Tap Login button

# Set up guides

### Install Appium Server
Use to interact with the mobile application

### Install Appium Inspector
Use to find elements' locator

### Install App package finder in Android
To find app package name

### Install dependencies for project

- virtualenv venv (Init virtual environment)
- source venv/bin/activate (Activate virtual environment)
- pip install -r requirements.txt
- venv/bin/python3 vsee_app_testing.py