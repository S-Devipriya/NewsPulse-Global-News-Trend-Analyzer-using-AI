from flask import Flask, render_template, request
import mysql.connector as mysql
from Text_Preprocessor import preprocess_text
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def NewsPulse():
    search_query = request.args.get('search', '')
    try:
        connection = mysql.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            database = "news_db"
        )
        cursor = connection.cursor(dictionary=True)
        
        if search_query:
            cleaned_search_query = preprocess_text(search_query)
            
            if cleaned_search_query:
                sql_query = "SELECT title, description, url, image_url, publishedAt, source_name FROM news_data WHERE "
                sql_query += "title LIKE %s OR description LIKE %s"
                sql_query += " ORDER BY publishedAt DESC"
                
                cursor.execute(sql_query, (f"%{cleaned_search_query}%", f"%{cleaned_search_query}%"))
            else:
                articles = []
        else:
            sql_query = "SELECT title, description, url, image_url, publishedAt, source_name FROM news_data ORDER BY publishedAt DESC"
            cursor.execute(sql_query)
            
        articles = cursor.fetchall() if 'articles' not in locals() else articles
        connection.close()
        
        return render_template('index.html', articles=articles, search_query=search_query)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)