# Password Manager Twilio App

This is a pretty simple webapp that allows you to get your passwords by texting a search string to a Twilio phone number. The app is based on Flask and uses PGP to decrypt a file and then do a quick string search for the texted term.

To start, install the requirements in requirements.txt, create a .env file (.env.sample provided), and run/deploy the app.

At the moment I'm just having fun so the code is messy and it hasn't been deployed but can be tested end-to-end using [ngrok](https://ngrok.com).
