import json
import urllib.request
import mysql.connector as mysql
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

apikey = API_KEY
category = "general"
url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&max=20&apikey={apikey}"

connection = mysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS news_db")
cursor.execute("USE news_db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS news_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        url VARCHAR(255),
        image_url LONGTEXT,
        publishedAt DATETIME,
        source_name VARCHAR(100),
        source_url VARCHAR(255)
    )
""")

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]

    for i in range(len(articles)):
        published_at_str = articles[i]['publishedAt']
        try:
            published_at = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ")
        except Exception:
            published_at = None
        cursor.execute("""
            INSERT INTO news_data (title, description, url, image_url, publishedAt, source_name, source_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            articles[i]['title'],
            articles[i]['description'],
            articles[i]['url'],
            articles[i]['image'],
            published_at,
            articles[i]['source']['name'],
            articles[i]['source']['url']
        ))
    connection.commit()
connection.close()

