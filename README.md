# NewsPulse Global News Trend Analyzer using AI

NewsPulse is an AI powered platform to collect, analyze and visualize trending topics from global news sources in real time. This project was created in fulfillment of the requirements for Infosys Virtual Internship 6.0. It for demonstration purposes and is a development build.

## Setting up Database
This project uses MYSQL as database and requires connection to MYSQL server. You can use MYSQL Workbench 8.0 CE. Database is automatically created on running the app.

## Setting up Environment Variables
Follow these steps to set up environment variables:
- Copy [.env.example](https://github.com/S-Devipriya/NewsPulse-Global-News-Trend-Analyzer-using-AI/tree/main/.env.example) file into a `.env file`
- Replace the placeholder values in the copied file to your actual credentials for MYSQL database and GNews API

## Running the app (current version)
- Run [News_Data_Collection.py](https://github.com/S-Devipriya/NewsPulse-Global-News-Trend-Analyzer-using-AI/tree/main/data/News_Data_Collection.py) atleast once
- Run [News_Data_App.py](https://github.com/S-Devipriya/NewsPulse-Global-News-Trend-Analyzer-using-AI/tree/mainnewspulse/News_Data_App.py)
- From Command line, open the http link in a browser to see the results
