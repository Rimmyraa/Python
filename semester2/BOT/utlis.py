import re

def check_query(input_text):
    # Define the allowed characters using regular expressions
    allowed_characters = re.compile(r'^[a-zA-Zа-яА-ЯіїэєґІЇЭЄ.,\s]*$')
    
    # Check if the input text matches the allowed pattern
    if allowed_characters.match(input_text):
        return True
    else:
        return False



