import pandas as pd
from transformers import pipeline

def get_latest_file(directory, prefix):
	import os
	files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.csv')]
	latest_file = max(files, key=os.path.getctime)
	return latest_file

def perform_sentiment_analysis(data_directory, prefix):
	# Step 1: Read the latest processed CSV file
	latest_file = get_latest_file(data_directory, prefix)
	data = pd.read_csv(latest_file)

	# Step 2: Handle NaN values by replacing them with an empty string
	data['Description'] = data['Description'].fillna('')

	# Step 3: Perform Sentiment Analysis on 'Description' column using Hugging Face transformers
	sentiment_analyzer = pipeline('sentiment-analysis')

	# Analyze sentiment for each description
	data['Sentiment'] = data['Description'].apply(lambda x: sentiment_analyzer(x)[0]['label'])

	# Save the results to a new CSV file
	output_file = latest_file.replace('.csv', '_with_sentiment.csv')
	data.to_csv(output_file, index=False)

	print(f"Sentiment analysis completed. Results saved to {output_file}")

# Example usage
if __name__ == "__main__":
	data_directory = 'nlp_pipeline/data'
	prefix = 'news_processed_'
	perform_sentiment_analysis(data_directory, prefix)