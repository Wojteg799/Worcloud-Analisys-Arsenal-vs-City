"""Data loading utilities for reading text files."""

import os


def load_text_file(file_path):
    """
    Load text from a file.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        str: Content of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")
