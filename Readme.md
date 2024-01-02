![wordcloud_image.png](wordcloud_image.png)

# Word Cloud Generator for YouTuber Types and Fan Counts

This Python script generates a visually appealing word cloud based on YouTuber types and their corresponding fan counts. Users can input a list of YouTuber types and fan counts, and the script will create a word cloud image using the wordcloud library and display it using matplotlib.pyplot.

## Getting Started

### Prerequisites
Make sure you have the required Python libraries installed. You can install them using the following command:

<pre>
pip install matplotlib wordcloud
</pre>

### Usage
Run the script by executing the following command in your terminal:

<pre>
python wordcloud_generator.py
</pre>

1. Enter the YouTuber types when prompted. Separate the types by commas.
2. Enter the corresponding fan counts when prompted. Separate the counts by commas.
3. The script will generate a word cloud and display it using matplotlib.pyplot. 

The resulting image will also be saved in the default location as "wordcloud_image.png".

### Example Usage
<pre>
Enter the types separate by ',':Gamer,Vlogger,Tech Reviewer,Comedian,Beauty Guru
You entered: ['Gamer', 'Vlogger', 'Tech Reviewer', 'Comedian', 'Beauty Guru']
Enter the counts separate by ',': 1000000, 800000, 1200000, 600000, 900000
You entered: [1000000, 800000, 1200000, 600000, 900000]
</pre>

## Notes
1. The script uses a system font for the word cloud display.
2. The WordCloud is generated with specific parameters, including width, height, background color, font path, and colormap.
3. The resulting word cloud image is displayed using matplotlib.pyplot.
4. The image is saved to the specified file path or the default path if not provided.