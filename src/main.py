"""Main application for wordcloud analysis of Arsenal vs Manchester City."""

import os
import nltk
import config
from data_loader import load_text_file
from text_processor import clean_text, tokenize_and_remove_stopwords
from wordcloud_generator import (
    get_word_frequencies,
    create_wordcloud,
    find_unique_terms,
    find_common_terms
)
from visualizer import save_wordcloud


def download_nltk_resources():
    """Download required NLTK resources."""
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)


def main():
    """Main function to run the wordcloud analysis."""
    print("Starting wordcloud analysis...")
    
    # Download NLTK resources
    download_nltk_resources()
    
    # Load data
    print("\nLoading text data...")
    arsenal_path = os.path.join(config.RAW_DATA_DIR, config.ARSENAL_FILE)
    city_path = os.path.join(config.RAW_DATA_DIR, config.CITY_FILE)
    
    text_arsenal = load_text_file(arsenal_path)
    text_city = load_text_file(city_path)
    
    # Clean text
    print("Cleaning text...")
    clean_arsenal = clean_text(text_arsenal)
    clean_city = clean_text(text_city)
    
    # Tokenize and remove stopwords
    print("Tokenizing and removing stopwords...")
    tokens_arsenal = tokenize_and_remove_stopwords(clean_arsenal)
    tokens_city = tokenize_and_remove_stopwords(clean_city)
    
    print(f"\nArsenal tokens: {len(tokens_arsenal)}")
    print(f"Manchester City tokens: {len(tokens_city)}")
    
    # Generate wordclouds for most frequent words
    print("\nGenerating wordclouds for most frequent words...")
    
    freq_arsenal = get_word_frequencies(tokens_arsenal)
    freq_city = get_word_frequencies(tokens_city)
    
    wordcloud_arsenal = create_wordcloud(freq_arsenal)
    wordcloud_city = create_wordcloud(freq_city)
    
    save_wordcloud(
        wordcloud_arsenal,
        'arsenal_most_frequent.png',
        'Arsenal - Most Frequent Words'
    )
    save_wordcloud(
        wordcloud_city,
        'city_most_frequent.png',
        'Manchester City - Most Frequent Words'
    )
    
    # Generate wordclouds for unique terms
    print("\nGenerating wordclouds for unique terms...")
    
    unique_arsenal = find_unique_terms(tokens_arsenal, tokens_city)
    unique_city = find_unique_terms(tokens_city, tokens_arsenal)
    
    print(f"Unique Arsenal terms: {len(set(unique_arsenal))}")
    print(f"Unique City terms: {len(set(unique_city))}")
    
    freq_unique_arsenal = get_word_frequencies(unique_arsenal)
    freq_unique_city = get_word_frequencies(unique_city)
    
    wordcloud_unique_arsenal = create_wordcloud(freq_unique_arsenal)
    wordcloud_unique_city = create_wordcloud(freq_unique_city)
    
    save_wordcloud(
        wordcloud_unique_arsenal,
        'arsenal_unique_terms.png',
        'Unique Terms - Arsenal'
    )
    save_wordcloud(
        wordcloud_unique_city,
        'city_unique_terms.png',
        'Unique Terms - Manchester City'
    )
    
    # Generate wordcloud for common terms
    print("\nGenerating wordcloud for common terms...")
    
    common_tokens = find_common_terms(tokens_arsenal, tokens_city)
    print(f"Common terms: {len(set(common_tokens))}")
    
    freq_common = get_word_frequencies(common_tokens)
    wordcloud_common = create_wordcloud(freq_common)
    
    save_wordcloud(
        wordcloud_common,
        'arsenal_city_common_terms.png',
        'Common Terms - Arsenal & Manchester City'
    )
    
    print("\n[SUCCESS] Analysis complete! All wordclouds saved to outputs directory.")


if __name__ == '__main__':
    main()
