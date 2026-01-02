# Wordcloud Analysis - Arsenal vs Manchester City

A modular Python application for generating wordcloud visualizations from text data comparing Arsenal and Manchester City.

## Project Structure

```
Worcloud-Analisys-Arsenal-vs-City/
├── data/
│   └── raw/
│       ├── Arsenal_text.txt
│       └── City_text.txt
├── outputs/              # Generated wordcloud images
├── src/
│   ├── config.py        # Configuration and settings
│   ├── data_loader.py   # File loading utilities
│   ├── text_processor.py    # Text cleaning and tokenization
│   ├── wordcloud_generator.py   # Wordcloud generation logic
│   ├── visualizer.py    # Output visualization
│   └── main.py          # Main application
└── requirements.txt     # Python dependencies
```

## Features

- **Text Processing**: Automated cleaning, tokenization, and stopword removal
- **Frequency Analysis**: Identifies most common words in each dataset
- **Comparative Analysis**: 
  - Unique terms for Arsenal
  - Unique terms for Manchester City
  - Common terms between both teams
- **Visualization**: High-quality wordcloud images (800x400, 300 DPI)
- **Modular Design**: Clean separation of concerns for easy maintenance

## Installation

```bash
# Install required packages
pip install -r requirements.txt
```

## Usage

```bash
# Run the analysis
python src/main.py
```

The script will:
1. Load text data from `data/raw/`
2. Clean and process the text
3. Generate 5 wordcloud visualizations
4. Save all outputs to `outputs/` directory

## Output Files

- `arsenal_most_frequent.png` - Top 50 frequent Arsenal words
- `city_most_frequent.png` - Top 50 frequent Manchester City words
- `arsenal_unique_terms.png` - Terms unique to Arsenal
- `city_unique_terms.png` - Terms unique to Manchester City
- `arsenal_city_common_terms.png` - Common terms between both teams

## Requirements

- Python 3.7+
- wordcloud >= 1.9.0
- matplotlib >= 3.5.0
- nltk >= 3.8.0

## Module Descriptions

### config.py
Centralized configuration for paths, file names, and wordcloud parameters.

### data_loader.py
Handles loading text files with proper error handling and encoding support.

### text_processor.py
Provides text cleaning and tokenization utilities:
- Removes punctuation, numbers, and special characters
- Filters out stopwords
- Normalizes text to lowercase

### wordcloud_generator.py
Core analysis functions:
- Calculates word frequencies
- Creates wordcloud objects
- Finds unique and common terms between datasets

### visualizer.py
Handles saving wordclouds as high-quality PNG images.

### main.py
Orchestrates the entire analysis workflow from data loading to output generation.

## License

See LICENSE file for details.
