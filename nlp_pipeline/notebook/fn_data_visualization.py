import pandas as pd
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
from datetime import datetime

def get_latest_file(directory, prefix):
	files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.csv')]
	latest_file = max(files, key=os.path.getctime)
	return latest_file

# Step 1: Read the latest processed CSV file
data_directory = 'data'
latest_file = get_latest_file(data_directory, 'news_processed_')
data = pd.read_csv(latest_file)

# Step 2: Generate Word Cloud for 'Description' column
# Handle NaN values by replacing them with an empty string
data['Description'] = data['Description'].fillna('')

text = ' '.join(description for description in data['Description'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Step 3: Save the Word Cloud image with a timestamp
image_directory = 'images'
os.makedirs(image_directory, exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
image_path = os.path.join(image_directory, f'word_cloud_{timestamp}.png')
wordcloud.to_file(image_path)

# Step 4: Display the Word Cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of News Descriptions')
# plt.show()

print(f"Word cloud image saved to {image_path}")