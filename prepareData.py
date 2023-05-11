import csv
import os
import re
from bs4 import BeautifulSoup


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ')
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text


def index_html_files(root_folder, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Content'])

        for root, _, files in os.walk(root_folder):
            for file in files:
                if file.endswith('.htm'):
                    file_path = os.path.join(root, file)
                    key = os.path.relpath(file_path, root_folder)
                    with open(file_path, 'r', encoding='utf-8') as html_file:
                        html_content = html_file.read()
                        content = extract_text_from_html(html_content)
                        writer.writerow([key, content])


root_folder = './data/manuals'  # Replace with the root folder path to parse
output_file = './data/structured-content.csv'  # Replace with the desired output CSV file path

index_html_files(root_folder, output_file)
