import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def get_latest_file(directory, prefix):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('.csv')]
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def visualize_sentiment_word_cloud(file_path, output_dir='images'):
    # Read the CSV file with sentiment analysis results
    data = pd.read_csv(file_path)

    # Print the columns to debug
    print("Columns in the CSV file:", data.columns)

    # Check if 'Title' column exists
    if 'Title' not in data.columns:
        raise KeyError("The column 'Title' does not exist in the CSV file.")

    # Separate positive and negative titles
    positive_titles = ' '.join(data[data['Sentiment'] == 'positive']['Title'])
    negative_titles = ' '.join(data[data['Sentiment'] == 'negative']['Title'])

    # Generate word clouds
    plt.figure(figsize=(16, 8))

    if positive_titles:
        positive_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(positive_titles)
        plt.subplot(1, 2, 1)
        plt.imshow(positive_wordcloud, interpolation='bilinear')
        plt.title('Positive Titles')
        plt.axis('off')
    else:
        print("No positive titles to generate word cloud.")

    if negative_titles:
        negative_wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds').generate(negative_titles)
        plt.subplot(1, 2, 2)
        plt.imshow(negative_wordcloud, interpolation='bilinear')
        plt.title('Negative Titles')
        plt.axis('off')
    else:
        print("No negative titles to generate word cloud.")

    # Save the plot as an image file if there are any word clouds generated
    if positive_titles or negative_titles:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, 'sentiment_word_cloud.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Sentiment word cloud saved to {output_file}")
    else:
        print("No word clouds generated due to lack of data.")

# Example usage
if __name__ == "__main__":
    data_directory = 'data'
    prefix = 'news_processed_'
    latest_file_with_sentiment = get_latest_file(data_directory, prefix)
    visualize_sentiment_word_cloud(latest_file_with_sentiment)