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

    Example Usage:
    ```python
    types = ["美食", "旅行", "健身", "美妆", "穿搭", "探店", "游戏", "电子产品推荐", "养生", "萌宠", "其他"]
    fan_counts = [43, 66, 36, 40, 87, 56, 61, 74, 60, 54, 5]
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

types = ["美食", "旅行", "健身", "美妆", "穿搭", "探店", "游戏", "电子产品推荐", "养生", "萌宠", "其他"]
fan_counts = [43, 66, 36, 40, 87, 56, 61, 74, 60, 54, 5]

save_path = "wordcloud_image.png"
generate_wordcloud(types, fan_counts)
