import re
import string
from nltk.corpus import stopwords


def clean_text(text):
    """
    Clean text by removing punctuation, single characters, numbers, and special characters.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned and lowercase text
    """
    # Remove punctuation
    temp = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    
    # Remove single characters
    temp = re.sub(r"\b\w\b", "", temp)
    
    # Remove numbers
    temp = re.sub(r"\d+", "", temp)
    
    # Remove special characters
    temp = re.sub(r"[#@\$%^\&*~+=<>|\\/{}`[\]]+", "", temp)
    
    # Remove multiple spaces
    temp = re.sub(r"\s{2,}", " ", temp)
    
    return temp.lower().strip()


def tokenize_and_remove_stopwords(text, language='english'):
    """
    Tokenize text and remove stopwords.
    
    Args:
        text (str): Cleaned text to tokenize
        language (str): Language for stopwords (default: 'english')
        
    Returns:
        list: List of tokens with stopwords removed
    """
    stop_words = set(stopwords.words(language))
    tokens = [token for token in text.split() if token not in stop_words]
    return tokens
