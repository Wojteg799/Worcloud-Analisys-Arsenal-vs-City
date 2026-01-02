import os
import matplotlib.pyplot as plt
import config


def save_wordcloud(wordcloud, filename, title):
    """
    Save a wordcloud as an image file.
    
    Args:
        wordcloud (WordCloud): WordCloud object to visualize
        filename (str): Output filename (without path)
        title (str): Title for the wordcloud
    """
    output_path = os.path.join(config.OUTPUT_DIR, filename)
    
    plt.figure(figsize=config.FIGURE_SIZE)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Saved wordcloud: {output_path}")
