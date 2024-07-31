import requests
import csv
from datetime import datetime

# Define the API endpoint and your API key
url = 'https://newsapi.org/v2/top-headlines'
api_key = 'b07207e5e7b44e5fb0fd275f501390a1'  # Replace with your actual API key

# Define the parameters for the request
params = {
	'country': 'us',  # You can change the country code as needed
	'pageSize': 100,  # Fetch around 100 articles
	'apiKey': api_key
}

# Make the request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
	# Parse the JSON response
	news_data = response.json()
	
	# Get the current date and time for the filename
	now = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"data/news_raw_{now}.csv"
	
	# Save the news articles to a CSV file
	with open(filename, mode='w', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(['Title', 'Description', 'URL'])  # Write the header
		
		for article in news_data['articles']:
			writer.writerow([article['title'], article['description'], article['url']])
	
	print(f"News articles saved to {filename}")
else:
	print(f"Failed to fetch news: {response.status_code}")
