import pandas as pd
import matplotlib.pyplot as plt
import os

def get_latest_file(directory, prefix):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith(prefix) and f.endswith('_with_sentiment.csv')]
    latest_file = max(files, key=os.path.getctime)
    return latest_file


def visualize_sentiment_pie_chart(file_path, output_dir='images'):
    # Read the CSV file with sentiment analysis results
    data = pd.read_csv(file_path)

    # Count the number of positive and negative sentiments
    sentiment_counts = data['Sentiment'].value_counts()

    # Plot the sentiment distribution as a pie chart
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Sentiment Distribution of News Descriptions')
    plt.ylabel('')  # Hide the y-label

    # Save the plot as an image file
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, 'sentiment_pie_chart.png')
    plt.savefig(output_file)
    plt.close()

    print(f"Sentiment pie chart saved to {output_file}")

# Example usage
if __name__ == "__main__":
    data_directory = 'data'
    prefix = 'news_processed_'
    latest_file_with_sentiment = get_latest_file(data_directory, prefix)
    visualize_sentiment_pie_chart(latest_file_with_sentiment)