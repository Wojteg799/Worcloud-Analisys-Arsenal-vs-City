"""Configuration file for wordcloud analysis project."""

import os

# Project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Output directory
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'outputs')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Input file names
ARSENAL_FILE = 'Arsenal_text.txt'
CITY_FILE = 'City_text.txt'

# Wordcloud settings
WORDCLOUD_WIDTH = 800
WORDCLOUD_HEIGHT = 400
WORDCLOUD_BACKGROUND = 'white'
TOP_N_WORDS = 50

# Visualization settings
FIGURE_SIZE = (10, 5)
