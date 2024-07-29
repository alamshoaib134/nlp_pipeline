import csv
import os
from datetime import datetime

def get_latest_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith('news_raw_') and f.endswith('.csv')]
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def read_articles(file_path):
    articles = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            articles.append(row)
    return articles

def preprocess_articles(articles):
    preprocessed_articles = []
    for article in articles:
        title = article[0].strip()
        description = article[1].strip() if len(article) > 1 else ''
        url = article[2].strip() if len(article) > 2 else ''
        if title:
            preprocessed_articles.append([title, description, url])
    return preprocessed_articles

def save_to_csv(articles, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description', 'URL'])
        writer.writerows(articles)

def main():
    data_directory = 'nlp_pipeline/data'
    latest_file = get_latest_file(data_directory)
    articles = read_articles(latest_file)
    preprocessed_articles = preprocess_articles(articles)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{data_directory}/news_preprocessed_{now}.csv"
    save_to_csv(preprocessed_articles, filename)
    print(f"Preprocessed news articles saved to {filename}")

if __name__ == "__main__":
    main()