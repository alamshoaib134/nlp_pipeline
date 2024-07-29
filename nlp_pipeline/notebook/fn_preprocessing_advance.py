import csv
import os
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure you have the necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def get_latest_file(directory, prefix):
	files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.csv')]
	latest_file = max(files, key=os.path.getctime)
	return latest_file

def read_articles(filename):
	articles = []
	with open(filename, mode='r', encoding='utf-8') as file:
		reader = csv.reader(file)
		next(reader)  # Skip header
		for row in reader:
			articles.append(row)
	return articles

def preprocess_text(text):
	# Tokenization
	tokens = word_tokenize(text)
	
	# Stopword Removal
	stop_words = set(stopwords.words('english'))
	tokens = [word for word in tokens if word.lower() not in stop_words]
	
	# Lemmatization
	lemmatizer = WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(word) for word in tokens]
	
	return ' '.join(tokens)

def process_articles(articles):
	processed_articles = []
	for article in articles:
		title = preprocess_text(article[0])
		description = preprocess_text(article[1])
		url = article[2]
		processed_articles.append([title, description, url])
	return processed_articles

def save_to_csv(articles, filename):
	with open(filename, mode='w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(['Title', 'Description', 'URL'])
		writer.writerows(articles)

def main():
	data_directory = 'data'
	latest_file = get_latest_file(data_directory, 'news_preprocessed_')
	articles = read_articles(latest_file)
	processed_articles = process_articles(articles)
	now = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"{data_directory}/news_processed_{now}.csv"
	save_to_csv(processed_articles, filename)
	print(f"Processed news articles saved to {filename}")

if __name__ == "__main__":
	main()