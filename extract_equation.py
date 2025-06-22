import re

def extract_equation(text):
    match = re.search(r'([\w\s\^\*\+\-/=\.]+=[\w\s\^\*\+\-/=\.]+)', text)
    if match:
        return match.group(1)
    math_words = re.sub(r'[^\dxX\+\-\*/=\^\s]', '', text)
    if any(char.isdigit() for char in math_words):
        return math_words.strip()
    return None
