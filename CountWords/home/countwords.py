import re
from collections import Counter
import socket
import os

def count_words(filename):
    """Count total number of words in a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)
    return len(words), words

def get_top_words(word_list, top_n=3):
    """Get the most frequent words and their counts."""
    counter = Counter(word_list)
    return counter.most_common(top_n)

def handle_apostrophes(text):
    """Handle apostrophes by splitting words with apostrophes into two words."""
    text = re.sub(r"(\w+)'(\w+)", r"\1 \2", text)
    return text

def get_ip_address():
    """Get the IP address of the machine running the container."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    file1_path = os.path.join(script_dir, 'data', 'IF-1.txt')
    file2_path = os.path.join(script_dir, 'data', 'AlwaysRememberUsThisWay-1.txt')
    output_file_path = os.path.join(script_dir, 'data', 'output', 'result.txt')
    
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    total_words_file1, words_file1 = count_words(file1_path)
    total_words_file2, words_file2 = count_words(file2_path)

    top_words_file1 = get_top_words(words_file1)

    with open(file2_path, 'r', encoding='utf-8') as file2:
        file2_text = file2.read()
    handled_text = handle_apostrophes(file2_text)
    words_file2_handled = re.findall(r'\b\w+\b', handled_text)
    top_words_file2 = get_top_words(words_file2_handled)

    ip_address = get_ip_address()

    result = [
        f"Total words in {file1_path}: {total_words_file1}",
        f"Total words in {file2_path}: {total_words_file2}",
        f"Grand total: {total_words_file1 + total_words_file2}",
        f"Most frequent words in {file1_path}: {top_words_file1}",
        f"Most frequent words in {file2_path}: {top_words_file2}",
        f"IP Address of the machine running the container: {ip_address}",
    ]

    with open(output_file_path, 'w', encoding='utf-8') as result_file:
        result_file.write("\n".join(result))

    with open(output_file_path, 'r', encoding='utf-8') as result_file:
        print(result_file.read())

if __name__ == '__main__':
    main()
