# m4rvyn3

A quirky little chat bot named M4rvyn3 - inspired by the Hitchhiker's Guide to the Galaxy who now lives on Twitter. Try not to take him too seriously.
https://twitter.com/m4rvyn3

## Components
1. Azure Logic App

This one 'watches' Twitter for mentions of the user handle, then sends the info to an API handler, written in Python

2. API (Python)

Handles the response to the mention. Hosted on Azure App Service

3. Random Tweets (Python)

Creates a random tweet every once in a while and posts it. Runs on the shell in a SCREEN
