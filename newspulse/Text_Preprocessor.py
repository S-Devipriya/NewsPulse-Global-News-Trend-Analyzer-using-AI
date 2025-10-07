import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocesses a search query string by:
    1. Converting to lowercase.
    2. Removing punctuation and numbers.
    3. Tokenizing the text (splitting into words).
    4. Removing common English stop words.
    5. Applying stemming to find the root of each word.
    
    Returns a list of processed keywords.
    """
    if not text:
        return []

    # 1. Lowercase
    text = text.lower()

    # 2. Remove numbers and punctuation
    text = re.sub(r'[\d\W_]+', ' ', text)

    # 3. Tokenize
    tokens = text.split()

    # 4. Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # 5. Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    return stemmed_tokens
