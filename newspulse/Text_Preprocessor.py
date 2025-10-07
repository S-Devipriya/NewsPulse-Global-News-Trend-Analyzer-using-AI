import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocesses a search query string by:
    1. Converting to lowercase.
    2. Removing punctuation and numbers.
    3. Correcting spelling using TextBlob.
    4. Tokenizing the text (splitting into words).
    5. Removing common English stop words.
    6. Join tokens back into a single string.
    
    Returns preprocessed and cleaned text.
    """
    if not text:
        return []

    # 1. Lowercase
    text = text.lower()

    # 2. Remove numbers and punctuation
    text = re.sub(r'[\d\W_]+', ' ', text)

    # 3. Spell Correction using TextBlob
    text = str(TextBlob(text).correct())

    # 4. Tokenize
    tokens = text.split()

    # 5. Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    #6. Join tokens back into a single string
    cleaned_string = ' '.join(tokens)

    return cleaned_string

