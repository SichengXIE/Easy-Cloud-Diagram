import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_wordcloud(types, counts):
    """
    Generate a visually appealing word cloud based on YouTuber types and fan counts.

    Parameters:
    - types: List of YouTuber types
    - counts: List of corresponding fan counts
    - save_path: (Optional) Path to save the image file. Default is "wordcloud_image.png".

    Dependencies:
    - WordCloud: The WordCloud class is used from the `wordcloud` library.
    - matplotlib.pyplot: Matplotlib is used for creating the plot.
    """
    words = {types[i]: counts[i] for i in range(len(types))}

    # Use a system font
    font_path = "/System/Library/Fonts/STHeiti Medium.ttc"

    # Generate word cloud diagram
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path,
                          colormap='Blues_r').generate_from_frequencies(words)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Save Path
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.2)
    plt.show()


def inputs():
    """
        Take user input for YouTuber types and fan counts.

        Returns:
        - input_type: List of YouTuber types
        - count_list: List of corresponding fan counts
    """
    inputtypes = input("Enter the types separate by ',': ")
    input_type = inputtypes.split(',')
    print(f"You entered: {input_type}")

    inputcounts = input("Enter the counts separate by ',': ")
    count_list = inputcounts.split(',')
    try:
        # Convert each string in the list to an integer
        count_list = [int(num) for num in count_list]
        print(f"You entered: {count_list}")

    except ValueError:
        print("Invalid input. Please enter a valid list of integers.")

    return input_type, count_list


if __name__ == "__main__":
    """
    Example Usage:
    ```
    types = ['Gamer', 'Vlogger', 'Tech Reviewer', 'Comedian', 'Beauty Guru']
    fan_counts = [1000000, 800000, 1200000, 600000, 900000]
    save_path = "wordcloud_image.png"
    generate_wordcloud(types, fan_counts, save_path)
    ```

    Note:
    - The function uses a system font for the word cloud display.
    - The WordCloud is generated using the `wordcloud` library, with specified width, height, background color,
      font path, and colormap.
    - The resulting word cloud image is displayed using matplotlib.pyplot.
    - The image is saved to the specified file path.

    :param types: List of YouTuber types
    :param counts: List of corresponding fan counts
    :param save_path: Path to save the image file (default is "wordcloud_image.png").
    
    """
    # Get user input
    types, counts = inputs()

    # Set default save path
    save_path = "wordcloud_image.png"

    # Generate and display word cloud
    generate_wordcloud(types, counts)
