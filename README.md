# NewsPulse Global News Trend Analyzer using AI

NewsPulse is an AI powered platform to collect, analyze and visualize trending topics from global news sources in real time. This project was created in fulfillment of the requirements for Infosys Virtual Internship 6.0. It for demonstration purposes and is a development build.

# Setting up Database
This project uses MYSQL as database and requires connection to MYSQL server. You can use MYSQL Workbench 8.0 CE. Database is automatically created on running the app.

# Setting up Environment Variables
Follow these steps to set up environment variables:
- Copy .env.example file into a .env file
- Replace the placeholder values in the copied file to your actual credentials for MYSQL database and GNews API

# Running the app (current version)
- Run data\News_Data_Collection.py atleast once
- Run newspulse\News_Data_App.py
- From Command line, go to the http link to see the results
