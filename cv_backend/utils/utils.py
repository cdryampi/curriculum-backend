from bs4 import BeautifulSoup
import re

def truncate_html_content(html_content, word_limit=15):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract text from the parsed HTML
    text = soup.get_text(' ')
    # Use regex to find individual words
    words = re.findall(r'\w+', text)
    # Check if we need to add ellipsis
    if len(words) > word_limit:
        truncated_text = ' '.join(words[:word_limit]) + '...'
    else:
        truncated_text = ' '.join(words)
    
    # Now reconstruct the HTML with truncated text
    # This is a basic approach and might need adjustments based on the complexity of your HTML
    for tag in soup.find_all(text=True):
        original_text = tag
        # Replace the text in each tag with truncated text
        tag.replace_with(truncated_text)
        break  # We replace the first portion of text we find and then stop

    # Return modified HTML as a string
    return str(soup)
