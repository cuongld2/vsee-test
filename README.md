# End to end test
Currently gmail prohibit automation to interact with gmail user interface. So I only manage to click login but after the login, gmail shows account page in the state of unauthenticated user.

Moreover, gmail does not allow to use imap protocol to read gmail content.

Hence, I only implement end-to-end test just for demonstration of how to implement end to end test with python and Selenium, with page object model design pattern set up in place.

Details for how to run the end-to-end test please read the README file. (Note that it needs .env file too, so please add the .env file to the root folder of the end-to-end test).

# Gmail SDK
To fulfill the requirements to interact with gmail, I use the python gmail sdk instead.
In order to run the project, please add the token.json and credentials.json into the gmail sdk folder

# API github interaction
Please follow the README in github interaction and add .env in order to use the API token in requests authorization

# Mobile Testing
I'm unable to open the vsee app using Appium due to the following error
```
UnknownError: An unknown server-side error occurred while processing the command. Original error: Cannot start the 'com.vsee.vsee.beta' application. Visit https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/android/activity-startup.md for troubleshooting. Original error: Cannot start the 'com.vsee.vsee.beta' application. Visit https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/android/activity-startup.md for troubleshooting. Original error: Activity name '.com.vsee.vsee.beta.MainActivity' used to start the app doesn't exist or cannot be launched! Make sure it exists and is a launchable activity
    at getResponseForW3CError (/tmp/.mount_Appiumiash84/resources/app/node_modules/appium/node_modules/appium-base-driver/lib/protocol/errors.js:804:9)
    at asyncHandler (/tmp/.mount_Appiumiash84/resources/app/node_modules/appium/node_modules/appium-base-driver/lib/protocol/protocol.js:380:37)
```
Hence, I use the "thecofeehouse" application instead
Details for how to run the test please refer to README.md file inside that folder