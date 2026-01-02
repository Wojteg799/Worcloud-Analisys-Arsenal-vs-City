
from collections import Counter
from wordcloud import WordCloud
import config


def get_word_frequencies(tokens, top_n=None):
    """
    Get word frequencies from a list of tokens.
    
    Args:
        tokens (list): List of word tokens
        top_n (int): Number of top words to return (default: from config)
        
    Returns:
        dict: Dictionary of word frequencies
    """
    if top_n is None:
        top_n = config.TOP_N_WORDS
    
    counter = Counter(tokens).most_common(top_n)
    return dict(counter)


def create_wordcloud(word_frequencies):
    """
    Create a WordCloud object from word frequencies.
    
    Args:
        word_frequencies (dict): Dictionary of word frequencies
        
    Returns:
        WordCloud: Generated wordcloud object
    """
    wordcloud = WordCloud(
        width=config.WORDCLOUD_WIDTH,
        height=config.WORDCLOUD_HEIGHT,
        background_color=config.WORDCLOUD_BACKGROUND
    ).generate_from_frequencies(word_frequencies)
    
    return wordcloud


def find_unique_terms(tokens_a, tokens_b):
    """
    Find terms that are unique to the first token set.
    
    Args:
        tokens_a (list): First list of tokens
        tokens_b (list): Second list of tokens
        
    Returns:
        list: Tokens unique to the first set
    """
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    
    unique_terms = [token for token in tokens_a if token in set_a - set_b]
    return unique_terms


def find_common_terms(tokens_a, tokens_b):
    """
    Find terms that are common between two token sets.
    
    Args:
        tokens_a (list): First list of tokens
        tokens_b (list): Second list of tokens
        
    Returns:
        list: Common tokens from both sets
    """
    set_a = set(tokens_a)
    set_b = set(tokens_b)
    
    common = list(set_a & set_b)
    common_tokens = [token for token in tokens_a + tokens_b if token in common]
    
    return common_tokens
